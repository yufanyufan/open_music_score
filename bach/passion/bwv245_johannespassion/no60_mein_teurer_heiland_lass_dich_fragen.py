with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV245')
        WorkTitle('Johannes-Passion')
    MovementNumber('60')
    MovementTitle('Mein teurer Heiland, laß dich fragen')
    with Identification():
        Creator('J.S.Bach', type='composer')
        Creator('Baroque Passion Oratorio', type='poet')
        Rights('by SkGnam')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.2)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2284.05)
            PageWidth(1615.83)
            with PageMargins(type='even'):
                LeftMargin(76.9231)
                RightMargin(76.9231)
                TopMargin(76.9231)
                BottomMargin(76.9231)
            with PageMargins(type='odd'):
                LeftMargin(76.9231)
                RightMargin(76.9231)
                TopMargin(76.9231)
                BottomMargin(76.9231)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('60. Aria. Mein teurer Heiland, laß dich fragen', default_x=76.9231, default_y=2107.12, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J.S.Bach - Johannes-Passion - BWV 245', default_x=1538.91, default_y=2107.12, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=6):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with Credit(page=7):
        CreditType('rights')
        CreditWords('by SkGnam', default_x=807.915, default_y=76.9231, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Basso\nSolo')
            PartAbbreviation('B.s')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Basso')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(2)
                MidiProgram(61)
                Volume(78.7402)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P2'):
            PartName('Soprani')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Boy Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(69.2913)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Alti')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(6)
                MidiProgram(1)
                Volume(69.2913)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Tenori')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(69.2913)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Bassi')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(8)
                MidiProgram(1)
                Volume(69.2913)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P6'):
            PartName('Organo')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Organo a canne')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(12)
                MidiProgram(20)
                Volume(21.2598)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Organo')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Organo a canne')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(9)
                MidiProgram(20)
                Volume(21.2598)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Organo')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Organo a canne')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(11)
                MidiProgram(20)
                Volume(21.2598)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Basso\nContinuo')
            PartAbbreviation('Bc.')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(3)
                MidiProgram(43)
                Volume(69.2913)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=483.51):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(77.76)
                        RightMargin(0.0)
                    TopSystemDistance(250.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_x=-47.37, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=67.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=398.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=502.62):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=78.53, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mein')
            with Note(default_x=120.78, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('teu')
            with Note(default_x=163.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=205.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
            with Note(default_x=247.53, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hei')
            with Note(default_x=289.78, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=8.78, default_y=-45.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('land,')
            with Note(default_x=374.27, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('laß')
                    Extend()
            with Note(default_x=416.52, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=458.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(-0.0)
                    SystemDistance(200.0)
            with Attributes():
                with Time():
                    Beats('12')
                    BeatType('8')
            with Note(default_x=123.59, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fra')
            with Note(default_x=154.47, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=185.34, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=247.1, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('laß')
            with Note(default_x=281.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=312.49, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fra')
            with Note(default_x=343.37, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=374.25, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=436.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('teu')
            with Note(default_x=468.55, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hei')
            with Note(default_x=48.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.15, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('land,')
            with Note(default_x=138.95, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('laß')
                    Extend()
            with Note(default_x=170.68, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=260.65, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fra')
            with Note(default_x=292.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=324.11, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=387.57, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('laß')
            with Note(default_x=422.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fra')
            with Note(default_x=53.98, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=90.15, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=162.5, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('teu')
            with Note(default_x=198.68, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
            with Note(default_x=234.85, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hei')
            with Note(default_x=307.2, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-50.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('land,')
            with Note(default_x=346.09, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('laß')
            with Note(default_x=382.27, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=418.44, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=91.21, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fra')
            with Note(default_x=147.62, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen:')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='8', width=403.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=524.78):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=81.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
            with Note(default_x=125.75, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=169.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.07, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=258.23, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
            with Note(default_x=302.38, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text("an's")
            with Note(default_x=390.7, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kreuz')
                    Extend()
            with Note(default_x=434.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=479.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=91.21, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-48.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schla')
            with Note(default_x=120.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.56, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.74, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=207.91, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.59, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=301.27, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-48.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note(default_x=347.95, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text("an's")
            with Note(default_x=394.63, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kreuz')
                    Extend()
            with Note(default_x=423.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=482.15, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=512.61, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=559.29, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=605.97, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=652.65, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schla')
            with Note(default_x=79.38, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-48.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note(default_x=133.37, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=187.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('selbst')
                    Extend()
            with Note(default_x=241.34, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=295.33, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=349.31, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sa')
            with Note(default_x=403.3, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-48.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('get:')
            with Note(default_x=470.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=524.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                    Extend()
            with Note(default_x=558.51, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=592.25, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=659.73, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=91.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bracht,')
                    Extend()
            with Note(default_x=205.39, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=319.2, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
            with Note(default_x=433.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                    Extend()
            with Note(default_x=504.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=575.28, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=689.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
            with Note(default_x=802.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.39, default_y=-40.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bracht!')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=450.46):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.19, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
            with Note(default_x=106.84, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=161.37, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
            with Note(default_x=201.02, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=240.68, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=319.99, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei')
                    Extend()
            with Note(default_x=359.64, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=384.43, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=409.21, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ge')
        with Measure(number='15', width=532.91):
            with Note(default_x=30.55, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('macht,')
            with Note(default_x=88.87, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
            with Note(default_x=131.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=173.7, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.12, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
            with Note(default_x=233.53, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(3)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=266.21, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=351.04, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=393.46, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei')
                    Extend()
            with Note(default_x=435.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=462.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=488.89, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=91.21, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('macht,')
            with Note(default_x=159.6, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
            with Note(default_x=193.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=227.99, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=262.19, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=296.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=330.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=364.77, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                    Extend()
            with Note(default_x=398.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=433.16, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei')
                    Extend()
            with Note(default_x=454.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=475.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=497.28, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('macht')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=249.05, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
            with Note(default_x=278.72, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=308.39, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=338.06, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=55.91, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.16, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                    Extend()
            with Note(default_x=164.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=202.71, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei')
            with Note(default_x=241.38, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=285.05, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('macht,')
            with Note(default_x=362.4, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
            with Note(default_x=401.07, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=91.21, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.4, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=265.76, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-41.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei')
                    Extend()
            with Note(default_x=302.13, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=338.49, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=396.67, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=423.25, default_y=5.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=455.92, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=11.2, default_y=-41.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('macht?')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='20', width=645.99):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=425.64, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kann')
            with Note(default_x=480.33, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-41.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=535.02, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=589.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=95.01, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=140.24, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.14, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.03, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
                    Extend()
            with Note(default_x=238.93, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=271.82, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pein')
            with Note(default_x=382.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=443.51, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=488.74, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=554.53, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=615.2, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=660.43, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=705.66, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=663.76):
            with Note(default_x=17.23, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.88, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=122.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=175.17, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=227.82, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.47, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mel')
            with Note(default_x=333.12, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('reich,')
                    Extend()
            with Note(default_x=366.02, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=398.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=451.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=504.22, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=556.87, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=609.51, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mel')
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=103.81, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('reich')
                    Extend()
            with Note(default_x=137.65, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.92, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=202.19, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er')
            with Note(default_x=234.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.96, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=345.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=365.19, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=397.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben?')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='24', width=410.61):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=61.91, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ist')
            with Note(default_x=97.73, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=146.98, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
            with Note(default_x=182.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
            with Note(default_x=218.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=254.44, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=290.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
            with Note(default_x=326.08, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lö')
            with Note(default_x=349.35, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=372.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('sung')
        with Measure(number='25', width=477.52):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.95, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('da,')
            with Note(default_x=50.15, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=86.49, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
            with Note(default_x=122.84, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
            with Note(default_x=159.18, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
            with Note(default_x=231.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-46.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lö')
            with Note(default_x=254.59, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.31, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.02, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=330.49, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=366.83, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=403.18, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=439.52, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('sung')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=91.21, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.95, default_y=-48.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('da,')
            with Note(default_x=135.03, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=178.86, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
            with Note(default_x=222.68, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
            with Note(default_x=266.5, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=310.32, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
            with Note(default_x=354.14, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-48.24, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lö')
            with Note(default_x=381.53, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.92, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=436.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=463.7, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=491.09, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=518.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=545.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=573.25, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=600.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=628.03, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=655.42, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.53, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.71, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.89, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.07, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.25, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=190.43, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.61, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.79, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.96, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.14, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.32, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=365.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=394.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=423.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=453.04, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=482.22, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=518.69, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=547.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=577.05, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=606.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=635.41, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=664.59, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=701.06, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=91.57, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('sung')
            with Note(default_x=203.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.95, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('da,')
            with Note(default_x=240.14, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=277.29, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
            with Note(default_x=314.43, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
            with Note(default_x=351.57, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=388.71, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
            with Note(default_x=425.85, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lö')
            with Note(default_x=463.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=486.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=509.42, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('sung')
                    Extend()
            with Note(default_x=538.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=11.39, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('da?')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='30', width=493.21):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=302.82, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=347.38, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=385.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('vor')
                    Extend()
            with Note(default_x=410.72, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.62, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=466.11, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=103.25, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmer')
            with Note(default_x=212.54, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('zen')
            with Note(default_x=267.19, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('zwar')
                    Extend()
            with Note(default_x=321.84, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=376.48, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('nichts')
            with Note(default_x=431.13, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=485.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-43.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
                    Extend()
            with Note(default_x=519.93, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=554.08, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('vor')
            with Note(default_x=608.73, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmer')
        with Measure(number='32', width=676.14):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.47, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.61, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=181.17, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.08, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.65, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.22, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=352.35, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=382.92, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=413.48, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=462.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('zen')
            with Note(default_x=511.3, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('zwar')
                    Extend()
            with Note(default_x=560.2, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=590.77, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=625.63, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('nichts')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(200.0)
            with Note(default_x=91.21, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=139.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
                    Extend()
            with Note(default_x=169.24, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.26, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('vor')
            with Note(default_x=247.28, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmer')
            with Note(default_x=361.32, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=409.34, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=457.36, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('zen')
            with Note(default_x=505.38, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('zwar')
            with Note(default_x=553.4, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('nichts')
                    Extend()
            with Note(default_x=583.42, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=613.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=65.96, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note(default_x=135.52, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=199.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei')
            with Note(default_x=247.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=295.3, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
            with Note(default_x=343.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=390.93, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                    Extend()
            with Note(default_x=495.27, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=517.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=553.02, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.96, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt,')
            with Note(default_x=600.84, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                    Extend()
            with Note(default_x=705.17, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=728.43, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=95.37, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.96, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt,')
            with Note(default_x=168.16, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=221.1, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei')
            with Note(default_x=274.04, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=340.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
                    Extend()
            with Note(default_x=373.3, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=406.38, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=439.47, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=472.55, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=525.49, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=578.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt')
                    Extend()
            with Note(default_x=631.37, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=684.3, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='36', width=677.41):
            with Note(default_x=37.15, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprichst,')
            with Note(default_x=109.58, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=162.25, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei')
            with Note(default_x=214.92, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.84, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
                    Extend()
            with Note(default_x=313.68, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=346.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=379.52, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=412.44, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=465.12, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=517.79, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt')
                    Extend()
            with Note(default_x=570.46, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=623.14, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(129.98)
            with Note(default_x=91.21, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprichts')
            with Note(default_x=198.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('still')
            with Note(default_x=256.46, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schwei')
            with Note(default_x=314.56, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=372.65, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.52, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend:')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=596.0, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.86, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ja,')
        with Measure(number='38', width=644.36):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=141.31, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.73, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=411.32, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=462.75, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei')
            with Note(default_x=514.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=546.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=578.47, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
                    Extend()
            with Note(default_x=610.62, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(129.98)
            with Note(default_x=91.21, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=191.76, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=242.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt,')
                    Extend()
            with Note(default_x=273.46, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.88, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.3, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.72, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.14, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=430.56, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=461.99, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=493.41, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=524.83, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=567.83, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprichst')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=718.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('still')
        with Measure(number='40', width=645.72):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwei')
            with Note(default_x=62.84, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.69, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.52, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend:')
            with Note(default_x=168.53, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.86, default_y=-51.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ja,')
            with Note(default_x=274.22, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('still')
            with Note(default_x=327.06, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schwei')
            with Note(default_x=379.9, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=432.75, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.52, default_y=-51.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=538.43, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('still')
            with Note(default_x=591.28, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    SystemDistance(129.98)
            with Note(default_x=91.21, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-58.26, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schwei')
            with Note(default_x=144.06, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=196.91, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.52, default_y=-58.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend:')
            with Note(default_x=249.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.4, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ja!')
            with Note(default_x=355.46, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch')
            with Note(default_x=408.31, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei')
            with Note(default_x=461.16, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=514.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('gest')
            with Note(default_x=566.86, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=619.71, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='42', width=689.24):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haupt')
                    Extend()
            with Note(default_x=67.13, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.45, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=173.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprichst')
            with Note(default_x=227.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('still')
            with Note(default_x=319.21, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=343.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=367.69, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-58.26, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schwei')
            with Note(default_x=421.01, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=474.34, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=527.67, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=580.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=634.32, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.52, default_y=-58.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend:')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(45.74)
                        RightMargin(0.0)
                    TopSystemDistance(80.0)
            with Note(default_x=91.21, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.4, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ja!')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='44', width=502.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=348.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P2'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=398.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=502.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Attributes():
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-59.62, relative_y=-29.81):
                        P()
                Sound(dynamics=57.78)
            with Note(default_x=312.49, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=405.12, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.99, default_y=-46.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=138.95, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=260.65, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa')
            with Note(default_x=355.84, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('rest')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.44, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-46.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('tot,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=403.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=524.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=187.36, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('best')
            with Note(default_x=349.31, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=524.77, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.54, default_y=-55.03, relative_y=-30.0):
                    Syllabic('single')
                    Text("ohn'")
                    Extend()
            with Note(default_x=625.99, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=91.21, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=802.54, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.49, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=450.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=532.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=112.56, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=201.57, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letz')
            with Note(default_x=278.72, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('To')
            with Note(default_x=164.03, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('des')
            with Note(default_x=284.69, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-49.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('not')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=645.99):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=338.14, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nir')
            with Note(default_x=480.33, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=95.01, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=271.82, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hin')
            with Note(default_x=349.95, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=403.4, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=443.15, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wen')
        with Measure(number='22', width=663.76):
            with Note(default_x=16.87, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=410.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=477.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=354.14, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('als')
            with Note(default_x=518.48, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir,')
            with Note(default_x=190.43, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=365.5, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=547.87, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=91.21, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-45.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('sühnt.')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=98.12, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=182.44, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-45.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trau')
            with Note(default_x=228.26, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=273.93, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
        with Measure(number='30', width=493.21):
            with Note(default_x=19.97, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-45.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=153.04, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=257.84, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-45.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('re!')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=676.14):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=361.32, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('gib')
            with Note(default_x=505.38, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.68, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur,')
            with Note(default_x=199.66, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=343.12, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=553.02, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=95.01, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.48, default_y=-41.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('dient,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='36', width=677.41):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=91.21, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-50.56, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
                    Extend()
            with Note(default_x=162.05, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.46, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.56, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=430.75, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.56, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=596.0, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='38', width=644.36):
            with Note(default_x=18.8, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.56, relative_y=-30.0):
                    Syllabic('middle')
                    Text('geh')
            with Note(default_x=308.1, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.3, default_y=-50.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('re.')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=645.72):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=689.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='44', width=502.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=348.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P3'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=398.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=502.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-59.62, relative_y=-29.81):
                        P()
                Sound(dynamics=57.78)
            with Note(default_x=312.49, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=405.12, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.99, default_y=-61.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-305.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=138.95, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=260.65, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa')
            with Note(default_x=355.84, default_y=-305.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('rest')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.44, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('tot,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=403.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=524.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.43)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-289.43):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=187.36, default_y=-309.43):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('best')
            with Note(default_x=349.31, default_y=-304.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=524.77, default_y=-304.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.33, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text("ohn'")
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.57, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-61.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=433.01, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=802.54, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.49, default_y=-61.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=450.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=532.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=112.56, default_y=-285.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=201.57, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letz')
            with Note(default_x=278.72, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('To')
            with Note(default_x=164.03, default_y=-305.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-68.77, relative_y=-30.0):
                    Syllabic('middle')
                    Text('des')
            with Note(default_x=284.69, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-68.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('not')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.08)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=645.99):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=338.14, default_y=-306.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nir')
            with Note(default_x=480.33, default_y=-311.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=271.82, default_y=-285.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hin')
            with Note(default_x=443.15, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-61.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wen')
        with Measure(number='22', width=663.76):
            with Note(default_x=16.87, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-61.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=410.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=477.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=354.14, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('als')
            with Note(default_x=518.48, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir,')
            with Note(default_x=190.43, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=365.5, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-61.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
                    Extend()
            with Note(default_x=453.04, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=500.46, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=547.87, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-61.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=635.41, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=682.82, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-54.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('sühnt.')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=98.12, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=182.44, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trau')
            with Note(default_x=273.93, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
        with Measure(number='30', width=493.21):
            with Note(default_x=19.97, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-54.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=80.52, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.95, default_y=-285.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.04, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=257.84, default_y=-290.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-54.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('re!')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=676.14):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=361.32, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('gib')
            with Note(default_x=505.38, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.68, default_y=-55.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur,')
            with Note(default_x=199.66, default_y=-300.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=343.12, default_y=-295.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=553.02, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=635.61, default_y=-305.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-310.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-61.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('dient')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='36', width=677.41):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=91.21, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
            with Note(default_x=256.46, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=430.75, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=596.0, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='38', width=644.36):
            with Note(default_x=19.16, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-63.05, relative_y=-30.0):
                    Syllabic('middle')
                    Text('geh')
            with Note(default_x=141.31, default_y=-305.85):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.1, default_y=-300.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.3, default_y=-63.05, relative_y=-30.0):
                    Syllabic('end')
                    Text('re.')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=645.72):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=689.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='44', width=502.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=348.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P4'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=398.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=502.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.75)
            with Attributes():
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-59.62, relative_y=-29.81):
                        P()
                Sound(dynamics=57.78)
            with Note(default_x=312.49, default_y=-402.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=405.12, default_y=-402.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.99, default_y=-44.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-402.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                    Extend()
            with Note(default_x=72.07, default_y=-402.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=110.81, default_y=-407.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.95, default_y=-412.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=193.76, default_y=-412.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=232.51, default_y=-417.75):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.65, default_y=-422.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa')
            with Note(default_x=355.84, default_y=-422.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('rest')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.44, default_y=-422.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('tot,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=403.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=524.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.49)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-383.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=187.36, default_y=-398.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('best')
            with Note(default_x=349.31, default_y=-418.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=524.77, default_y=-398.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.33, default_y=-40.91, relative_y=-30.0):
                    Syllabic('single')
                    Text("ohn'")
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.1)
            with Note(default_x=91.57, default_y=-390.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=433.01, default_y=-410.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=802.54, default_y=-405.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.49, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=450.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=532.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.27)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-396.27):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=112.56, default_y=-396.27):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=201.57, default_y=-396.27):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letz')
            with Note(default_x=278.72, default_y=-396.27):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-406.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('To')
            with Note(default_x=84.03, default_y=-406.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=129.74, default_y=-411.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.03, default_y=-411.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('des')
            with Note(default_x=284.69, default_y=-411.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('not')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.62)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=645.99):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=338.14, default_y=-407.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nir')
            with Note(default_x=480.33, default_y=-412.71):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.46)
            with Note(default_x=95.01, default_y=-442.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=271.82, default_y=-422.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hin')
            with Note(default_x=349.95, default_y=-432.46):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=443.51, default_y=-427.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wen')
            with Note(default_x=521.63, default_y=-427.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=575.09, default_y=-422.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=615.2, default_y=-417.46):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=663.76):
            with Note(default_x=16.87, default_y=-417.46):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=410.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=477.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.03)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=354.14, default_y=-400.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('als')
            with Note(default_x=518.48, default_y=-400.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-385.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir,')
            with Note(default_x=190.43, default_y=-395.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=365.5, default_y=-400.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=547.87, default_y=-400.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.36)
            with Note(default_x=91.21, default_y=-393.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('sühnt.')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=-393.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=98.12, default_y=-393.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=182.44, default_y=-393.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trau')
            with Note(default_x=273.93, default_y=-393.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
        with Measure(number='30', width=493.21):
            with Note(default_x=19.61, default_y=-388.36):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=257.84, default_y=-383.36):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.56, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('re!')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=676.14):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.95)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=361.32, default_y=-398.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('gib')
            with Note(default_x=505.38, default_y=-398.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-403.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur,')
                    Extend()
            with Note(default_x=100.74, default_y=-403.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.25, default_y=-408.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.66, default_y=-413.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=343.12, default_y=-393.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=553.02, default_y=-408.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=635.61, default_y=-403.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.34)
            with Note(default_x=95.01, default_y=-399.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('dient,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='36', width=677.41):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.44)
            with Note(default_x=91.21, default_y=-407.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
            with Note(default_x=256.46, default_y=-407.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=430.75, default_y=-402.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=596.0, default_y=-407.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='38', width=644.36):
            with Note(default_x=19.16, default_y=-402.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('geh')
            with Note(default_x=141.31, default_y=-407.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=224.88, default_y=-412.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.1, default_y=-417.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.3, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('re.')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=645.72):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=689.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='44', width=502.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=348.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P5'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=398.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=502.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.43)
            with Attributes():
                with Time(symbol='common'):
                    Beats('12')
                    BeatType('8')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-59.62, relative_y=-29.81):
                        P()
                Sound(dynamics=57.78)
            with Note(default_x=312.49, default_y=-505.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=405.12, default_y=-520.18):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.99, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-515.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=138.95, default_y=-510.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=260.65, default_y=-505.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa')
            with Note(default_x=355.84, default_y=-515.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('rest')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.44, default_y=-530.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-46.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('tot,')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=403.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=524.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-518.92):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=187.36, default_y=-513.92):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('best')
            with Note(default_x=349.31, default_y=-508.92):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
                    Extend()
            with Note(default_x=437.04, default_y=-503.92):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=524.77, default_y=-498.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.33, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text("ohn'")
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.21)
            with Note(default_x=91.57, default_y=-515.31):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=433.01, default_y=-510.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=802.54, default_y=-495.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.21, default_y=-51.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=450.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=532.91):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.06)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-484.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=112.56, default_y=-509.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=201.57, default_y=-504.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letz')
            with Note(default_x=278.72, default_y=-519.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-524.33):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('To')
            with Note(default_x=164.03, default_y=-519.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('des')
            with Note(default_x=284.69, default_y=-529.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('not')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.37)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=645.99):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=338.14, default_y=-512.08):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nir')
            with Note(default_x=480.33, default_y=-507.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gend')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.54)
            with Note(default_x=95.01, default_y=-532.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=271.82, default_y=-532.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hin')
            with Note(default_x=443.15, default_y=-527.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wen')
        with Measure(number='22', width=663.76):
            with Note(default_x=16.87, default_y=-542.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=410.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=477.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.97)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=354.14, default_y=-505.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('als')
            with Note(default_x=518.48, default_y=-500.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-495.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir,')
            with Note(default_x=190.43, default_y=-490.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=365.5, default_y=-485.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=547.87, default_y=-520.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.52)
            with Note(default_x=91.21, default_y=-495.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.34, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('sühnt.')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=-475.87):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=98.12, default_y=-510.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=182.44, default_y=-495.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trau')
            with Note(default_x=228.26, default_y=-490.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=273.93, default_y=-485.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
        with Measure(number='30', width=493.21):
            with Note(default_x=19.97, default_y=-495.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=153.04, default_y=-490.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=257.84, default_y=-510.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('re!')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=676.14):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.92)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=361.32, default_y=-491.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('gib')
            with Note(default_x=505.38, default_y=-501.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-521.87):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
            with Note(default_x=199.66, default_y=-516.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=343.12, default_y=-511.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=425.71, default_y=-506.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=553.02, default_y=-501.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ver')
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-514.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='36', width=677.41):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.92)
            with Note(default_x=91.21, default_y=-510.21):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-56.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
                    Extend()
            with Note(default_x=162.05, default_y=-505.21):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.46, default_y=-500.21):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=430.75, default_y=-510.21):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-56.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
                    Extend()
            with Note(default_x=525.16, default_y=-505.21):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=596.0, default_y=-510.21):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='38', width=644.36):
            with Note(default_x=19.16, default_y=-530.21):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-56.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('geh')
            with Note(default_x=141.31, default_y=-525.21):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.1, default_y=-510.21):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-56.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('re.')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=645.72):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=689.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='44', width=502.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=348.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P6'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=174.78, default_y=-42.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=206.77, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=238.77, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=270.76, default_y=-7.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.75, default_y=-10.5, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=334.74, default_y=-3.5, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=385.93, default_y=-21.0, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=385.93, default_y=-24.5, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=417.93, default_y=-17.5, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=449.92, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=398.1):
            with Note(default_x=10.0, default_y=-10.5, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=43.32, default_y=-3.5, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=96.63, default_y=-21.0, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=96.63, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=129.95, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=163.27, default_y=-10.5, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.59, default_y=-21.0, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=229.91, default_y=-14.0, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=263.22, default_y=-17.5, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=296.54, default_y=-17.5, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=329.86, default_y=-7.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=502.62):
            with Note(default_x=10.94, default_y=-10.5, dynamics=82.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.53, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.53, default_y=-21.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.78, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.28, default_y=-21.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.53, default_y=-28.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=332.02, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=374.27, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=416.52, default_y=-24.5, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=458.77, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-525.18)
            with Attributes():
                with Time():
                    Beats('12')
                    BeatType('8')
            with Note(default_x=123.59, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=185.34, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=216.22, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.1, default_y=-24.5, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=281.62, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=459.0):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=456.22):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=234.85, default_y=-14.0, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=307.2, default_y=-31.5, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.09, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=382.27, default_y=-21.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=418.44, default_y=-24.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.62, default_y=-28.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.87, default_y=-31.5, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=218.12, default_y=-17.5, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=253.38, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=288.63, default_y=-10.5, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=323.88, default_y=-3.5, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=380.29, default_y=-21.0, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=380.29, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=415.54, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=450.8, default_y=-7.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='8', width=403.82):
            with Note(default_x=10.0, default_y=-10.5, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=43.81, default_y=-3.5, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=97.91, default_y=-21.0, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=97.91, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=131.72, default_y=-7.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=165.54, default_y=-10.5, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=199.35, default_y=-21.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=233.16, default_y=-14.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=266.97, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.79, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=334.6, default_y=-7.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=524.78):
            with Note(default_x=10.94, default_y=-7.0, dynamics=82.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.59, default_y=-10.5, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=81.59, default_y=-17.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.75, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=214.07, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=258.23, default_y=-28.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=346.54, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=390.7, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=434.86, default_y=-24.5, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=479.02, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-518.92)
            with Note(default_x=91.21, default_y=-28.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=207.91, default_y=-14.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.59, default_y=-14.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=301.27, default_y=-17.5, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=347.95, default_y=-21.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=394.63, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=452.97, default_y=-7.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=512.61, default_y=-10.5, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=559.29, default_y=-10.5, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=652.65, default_y=-10.5, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='11', width=715.32):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-515.31)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=802.9, default_y=-31.5, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=916.72, default_y=-17.5, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=1030.53, default_y=-7.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=1144.34, default_y=-10.5, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=1258.16, default_y=-3.5, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=1414.65, default_y=-21.0, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=119.55, default_y=-7.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=147.89, default_y=-14.0, dynamics=62.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=176.23, default_y=-14.0, dynamics=62.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=204.57, default_y=-17.5, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=261.24, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.58, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=317.92, default_y=-24.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.26, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=402.94, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='14', width=450.46):
            with Note(default_x=12.66, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=67.19, default_y=-24.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
            with Note(default_x=161.37, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=201.02, default_y=-28.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=240.68, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.33, default_y=-10.5, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=319.99, default_y=-10.5, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=359.64, default_y=-14.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=409.21, default_y=-17.5, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='15', width=532.91):
            with Note(default_x=30.55, default_y=-14.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=88.87, default_y=-21.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.87, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=131.28, default_y=-21.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=216.12, default_y=-24.5, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=266.21, default_y=-24.5, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=308.62, default_y=-17.5, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=393.46, default_y=-21.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=435.87, default_y=-14.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=488.89, default_y=-10.5, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-529.33)
            with Note(default_x=91.21, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.41, default_y=-17.5, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=159.6, default_y=-14.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=193.8, default_y=-21.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=262.19, default_y=-28.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=296.38, default_y=-31.5, dynamics=56.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=330.58, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=364.77, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=398.97, default_y=-17.5, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=433.16, default_y=-21.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=475.91, default_y=-24.5, dynamics=56.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-24.5, dynamics=65.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=112.56, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=201.57, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=278.72, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=164.03, default_y=-31.5, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=284.8, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-522.08)
            with Note(default_x=91.21, default_y=-35.0, dynamics=54.44):
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
            with Note(default_x=149.4, default_y=-38.5, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.58, default_y=-24.5, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=265.76, default_y=-14.0, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=455.92, default_y=-14.0, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=514.1, default_y=-17.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=594.11, default_y=-10.5, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=594.11, default_y=-14.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=652.29, default_y=-10.5, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=710.47, default_y=-14.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='20', width=645.99):
            with Note(default_x=10.0, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=119.38, default_y=-14.0, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=174.07, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=228.76, default_y=-28.0, dynamics=52.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-552.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=663.76):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=280.47, default_y=-17.5, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=333.12, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=451.57, default_y=-28.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=504.22, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=609.51, default_y=-14.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.81, default_y=-17.5, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=137.65, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=169.92, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=202.19, default_y=-21.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=234.45, default_y=-24.5, dynamics=65.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=274.79, default_y=-28.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=324.85, default_y=-31.5, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=397.46, default_y=-28.0, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=429.72, default_y=-17.5, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=410.61):
            with Note(default_x=12.66, default_y=-17.5, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.91, default_y=-21.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
            with Note(default_x=146.98, default_y=-21.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.8, default_y=-24.5, dynamics=56.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=218.62, default_y=-24.5, dynamics=56.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=254.44, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=290.26, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=326.08, default_y=-21.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=326.08, default_y=-14.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=372.61, default_y=-31.5, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='25', width=477.52):
            with Note(default_x=13.8, default_y=-35.0, dynamics=56.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with Note(default_x=195.53, default_y=-21.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=231.87, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=277.31, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=330.49, default_y=-28.0, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=366.83, default_y=-24.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=403.18, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=403.18, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=439.52, default_y=-35.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-525.0)
            with Note(default_x=91.21, default_y=-38.5, dynamics=55.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=178.86, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=222.68, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=266.5, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=310.32, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
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
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='27', width=731.84):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-515.87)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=277.29, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=314.43, default_y=-38.5, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=351.57, default_y=-21.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=388.71, default_y=-28.0, dynamics=70.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=425.85, default_y=-24.5, dynamics=70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=463.0, default_y=-24.5, dynamics=70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=509.42, default_y=-21.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='29', width=359.85):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=493.21):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=440.62, default_y=-10.5, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.25, default_y=-24.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=212.54, default_y=-21.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=267.19, default_y=-14.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=376.48, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=431.13, default_y=-17.5, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=485.77, default_y=-24.5, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=554.08, default_y=-28.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=608.73, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=738.51, default_y=-24.5, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='32', width=676.14):
            with Note(default_x=10.0, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=58.91, default_y=-14.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.04, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=181.17, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=230.08, default_y=-28.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=352.35, default_y=-31.5, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=625.63, default_y=-31.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-521.87)
            with Note(default_x=91.21, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=139.23, default_y=-28.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.26, default_y=-21.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=247.28, default_y=-17.5, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=295.3, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=361.32, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='34', width=753.2):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-519.34)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note(default_x=274.04, default_y=-24.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=340.21, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=406.38, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=472.55, default_y=-24.5, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=525.49, default_y=-21.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=578.43, default_y=-17.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=631.37, default_y=-17.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=684.3, default_y=-17.5, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='36', width=677.41):
            with Note(default_x=37.15, default_y=-21.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=214.92, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.76, default_y=-31.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.6, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=412.44, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=465.12, default_y=-24.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=517.79, default_y=-21.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=570.46, default_y=-21.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=623.14, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-530.21)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=644.36):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=462.75, default_y=-31.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=514.18, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-31.5, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=141.49, default_y=-21.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=191.76, default_y=-24.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=242.04, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=304.88, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=367.72, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=430.56, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=461.99, default_y=-35.0, dynamics=76.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=493.41, default_y=-38.5, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=524.83, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=567.83, default_y=-31.5, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=618.11, default_y=-28.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=668.38, default_y=-49.0, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=718.66, default_y=-42.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=645.72):
            with Note(default_x=10.0, default_y=-24.5, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=62.84, default_y=-24.5, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.69, default_y=-21.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=168.53, default_y=-35.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=221.37, default_y=-35.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=274.22, default_y=-35.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=327.06, default_y=-35.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=432.75, default_y=-38.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
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
            with Note(default_x=249.76, default_y=-21.0, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=302.61, default_y=-28.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=355.46, default_y=-35.0, dynamics=51.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=408.31, default_y=-17.5, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=514.01, default_y=-21.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=566.86, default_y=-21.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=619.71, default_y=-28.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=672.56, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='42', width=689.24):
            with Note(default_x=13.8, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=67.13, default_y=-24.5, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.45, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=173.78, default_y=-21.0, dynamics=83.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=227.1, default_y=-28.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.43, default_y=-35.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=367.69, default_y=-17.5, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=421.01, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=474.34, default_y=-31.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=527.67, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-31.5, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=158.72, default_y=-42.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=200.92, default_y=-31.5, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=243.11, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=285.31, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=327.5, default_y=-10.5, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=369.7, default_y=-3.5, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=437.21, default_y=-17.5, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=437.21, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=521.6, default_y=-7.0, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='44', width=502.76):
            with Note(default_x=10.0, default_y=-10.5, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=52.34, default_y=-7.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.09, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.09, default_y=-14.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.43, default_y=-3.5, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.77, default_y=-7.0, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=247.11, default_y=-21.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.45, default_y=-17.5, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=331.8, default_y=-31.5, dynamics=53.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=374.14, default_y=-21.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=458.82, default_y=-28.0, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='45', width=348.1):
            with Note(default_x=12.66, default_y=-31.5, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P7'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=174.78, default_y=-42.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=206.77, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=238.77, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=270.76, default_y=-14.0, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.75, default_y=-17.5, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=385.93, default_y=-28.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=385.93, default_y=-24.5, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=449.92, default_y=-14.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=398.1):
            with Note(default_x=10.0, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.63, default_y=-28.0, dynamics=52.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=96.63, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=129.95, default_y=-14.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=163.27, default_y=-17.5, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.59, default_y=-31.5, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=263.22, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=296.54, default_y=-24.5, dynamics=64.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=329.86, default_y=-14.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=502.62):
            with Note(default_x=10.94, default_y=-17.5, dynamics=86.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.53, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.53, default_y=-21.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.78, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=163.03, default_y=-42.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=205.28, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.53, default_y=-42.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.78, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=332.02, default_y=-28.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=374.27, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=416.52, default_y=-42.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=458.77, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Time():
                    Beats('12')
                    BeatType('8')
            with Note(default_x=123.59, default_y=-42.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=154.47, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=185.34, default_y=-35.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=185.34, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=216.22, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=281.62, default_y=-35.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=312.49, default_y=-31.5, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=405.12, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-49.0, dynamics=57.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.99, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=95.15, default_y=-38.5, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=138.95, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.68, default_y=-42.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=260.65, default_y=-42.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=292.38, default_y=-45.5, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=324.11, default_y=-42.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=355.84, default_y=-38.5, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=387.57, default_y=-31.5, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=422.1, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.8, default_y=-31.5, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.98, default_y=-35.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=90.15, default_y=-24.5, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=126.33, default_y=-24.5, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=162.5, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=198.68, default_y=-35.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=234.85, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=307.2, default_y=-38.5, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.09, default_y=-42.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=418.44, default_y=-31.5, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-31.5, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=147.62, default_y=-38.5, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=147.62, default_y=-35.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.87, default_y=-31.5, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=218.12, default_y=-17.5, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=253.38, default_y=-14.0, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=288.63, default_y=-17.5, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=380.29, default_y=-28.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=380.29, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=450.8, default_y=-14.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='8', width=403.82):
            with Note(default_x=10.0, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.91, default_y=-28.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=97.91, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=131.72, default_y=-14.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=165.54, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.35, default_y=-31.5, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=266.97, default_y=-28.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=300.79, default_y=-24.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=334.6, default_y=-14.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=524.78):
            with Note(default_x=10.94, default_y=-17.5, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.59, default_y=-17.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.75, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=169.91, default_y=-42.0, dynamics=57.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=214.07, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=258.23, default_y=-42.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=302.38, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.54, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=390.7, default_y=-31.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=434.86, default_y=-42.0, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=479.02, default_y=-38.5, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-42.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=149.56, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.91, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=254.59, default_y=-24.5, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=301.27, default_y=-28.0, dynamics=70.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=394.63, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=452.97, default_y=-17.5, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=512.61, default_y=-17.5, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=559.29, default_y=-17.5, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=652.65, default_y=-17.5, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-21.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=187.36, default_y=-28.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=349.31, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=524.77, default_y=-31.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=592.25, default_y=-31.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=625.99, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
            with Note(default_x=659.73, default_y=-38.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.57, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=433.01, default_y=-35.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=575.28, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=689.09, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=802.9, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=916.72, default_y=-17.5, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=1030.53, default_y=-14.0, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=1144.34, default_y=-17.5, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=1414.65, default_y=-28.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-24.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=119.55, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=147.89, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=176.23, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=204.57, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=232.91, default_y=-24.5, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=261.24, default_y=-38.5, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.58, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=317.92, default_y=-31.5, dynamics=56.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=346.26, default_y=-31.5, dynamics=56.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=374.6, default_y=-28.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=402.94, default_y=-28.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='14', width=450.46):
            with Note(default_x=12.66, default_y=-31.5, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with Note(default_x=161.37, default_y=-31.5, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=201.02, default_y=-35.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=280.33, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=319.99, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=359.64, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=532.91):
            with Note(default_x=30.55, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=88.87, default_y=-31.5, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=131.28, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=216.12, default_y=-28.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=266.21, default_y=-31.5, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=308.62, default_y=-24.5, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=393.46, default_y=-28.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=488.89, default_y=-24.5, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-31.5, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=125.41, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.8, default_y=-28.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=262.19, default_y=-35.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=296.38, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=330.58, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=364.77, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=398.97, default_y=-28.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=-31.5, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=112.56, default_y=-31.5, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=142.23, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=171.9, default_y=-24.5, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=201.57, default_y=-28.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=278.72, default_y=-31.5, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-35.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=164.03, default_y=-38.5, dynamics=55.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=284.8, default_y=-42.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-42.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.4, default_y=-56.0, dynamics=91.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.58, default_y=-35.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=265.76, default_y=-24.5, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=396.67, default_y=-21.0, dynamics=86.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=455.92, default_y=-24.5, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=594.11, default_y=-17.5, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=594.11, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='20', width=645.99):
            with Note(default_x=10.0, default_y=-28.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.69, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.07, default_y=-28.0, dynamics=86.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=228.76, default_y=-35.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=338.14, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=480.33, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=95.01, default_y=-42.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=271.82, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=443.51, default_y=-28.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=615.2, default_y=-28.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='22', width=663.76):
            with Note(default_x=16.98, default_y=-38.5, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=227.82, default_y=-38.5, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=280.47, default_y=-24.5, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=333.12, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=451.57, default_y=-38.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=504.22, default_y=-42.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=556.87, default_y=-38.5, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=609.51, default_y=-28.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.81, default_y=-28.0, dynamics=87.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=169.92, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=202.19, default_y=-38.5, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=324.85, default_y=-42.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=365.19, default_y=-38.5, dynamics=70.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=429.72, default_y=-28.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=461.99, default_y=-24.5, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=494.26, default_y=-24.5, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=410.61):
            with Note(default_x=12.66, default_y=-24.5, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.91, default_y=-28.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
            with Note(default_x=146.98, default_y=-28.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.8, default_y=-31.5, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=218.62, default_y=-38.5, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=254.44, default_y=-28.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=290.26, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=326.08, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=326.08, default_y=-28.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=372.61, default_y=-38.5, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='25', width=477.52):
            with Note(default_x=13.8, default_y=-35.0, dynamics=56.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with Note(default_x=195.53, default_y=-35.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=231.87, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=277.31, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=330.49, default_y=-35.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=366.83, default_y=-35.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=403.18, default_y=-31.5, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=439.52, default_y=-42.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-45.5, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=178.86, default_y=-31.5, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=222.68, default_y=-35.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=354.14, default_y=-31.5, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=518.48, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=573.25, default_y=-28.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-24.5, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=73.71, default_y=-31.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.43, default_y=-28.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=365.5, default_y=-28.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=482.22, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=547.87, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=664.59, default_y=-42.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.32, default_y=-31.5, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=240.14, default_y=-31.5, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.29, default_y=-42.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=314.43, default_y=-45.5, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=388.71, default_y=-42.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=425.85, default_y=-42.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=509.42, default_y=-31.5, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='29', width=359.85):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=493.21):
            with Note(default_x=19.97, default_y=-24.5, dynamics=90.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=153.04, default_y=-28.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=258.2, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=347.38, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=385.23, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=440.62, default_y=-35.0, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.25, default_y=-38.5, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=212.54, default_y=-28.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=267.19, default_y=-21.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=376.48, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=431.13, default_y=-35.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=554.08, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=608.73, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=663.37, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=676.14):
            with Note(default_x=10.0, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=181.17, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=230.08, default_y=-38.5, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=291.22, default_y=-42.0, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=352.35, default_y=-38.5, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=625.63, default_y=-38.5, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=139.23, default_y=-42.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.26, default_y=-28.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=247.28, default_y=-28.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=361.32, default_y=-35.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=361.32, default_y=-31.5, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=505.38, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=553.4, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-31.5, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.52, default_y=-21.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=199.66, default_y=-21.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.48, default_y=-24.5, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=295.3, default_y=-28.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=343.12, default_y=-31.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=553.02, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=95.37, default_y=-35.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=168.16, default_y=-42.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=168.16, default_y=-28.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=221.1, default_y=-28.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=274.04, default_y=-38.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=340.21, default_y=-38.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=406.38, default_y=-42.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=472.55, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=525.49, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=578.43, default_y=-28.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=631.37, default_y=-24.5, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=684.3, default_y=-24.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='36', width=677.41):
            with Note(default_x=37.15, default_y=-28.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=214.92, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=280.76, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=346.6, default_y=-45.5, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=412.44, default_y=-35.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=465.12, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=517.79, default_y=-31.5, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=570.46, default_y=-28.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=623.14, default_y=-28.0, dynamics=74.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=256.46, default_y=-31.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=430.75, default_y=-31.5, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=596.0, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='38', width=644.36):
            with Note(default_x=19.16, default_y=-31.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=141.31, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=308.46, default_y=-42.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=462.75, default_y=-42.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=514.18, default_y=-31.5, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-38.5, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=242.04, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=304.88, default_y=-38.5, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=336.3, default_y=-42.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=367.72, default_y=-45.5, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=430.31, default_y=-42.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=668.38, default_y=-49.0, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=718.66, default_y=-42.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=645.72):
            with Note(default_x=10.0, default_y=-35.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
            with Note(default_x=168.53, default_y=-42.0, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=221.37, default_y=-45.5, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=274.22, default_y=-49.0, dynamics=52.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=327.06, default_y=-45.5, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
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
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
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
            with Note(default_x=249.76, default_y=-42.0, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=408.31, default_y=-31.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=461.16, default_y=-24.5, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=514.01, default_y=-31.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=566.86, default_y=-28.0, dynamics=83.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=619.71, default_y=-35.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=672.56, default_y=-31.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=672.56, default_y=-28.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='42', width=689.24):
            with Note(default_x=13.8, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=67.13, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.45, default_y=-45.5, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=173.78, default_y=-28.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=227.1, default_y=-35.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=280.43, default_y=-38.5, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=280.43, default_y=-42.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=367.69, default_y=-42.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=421.01, default_y=-42.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=474.34, default_y=-45.5, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=527.67, default_y=-42.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-42.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=158.72, default_y=-42.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=200.92, default_y=-31.5, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=243.11, default_y=-17.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=285.31, default_y=-14.0, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=327.5, default_y=-17.5, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=437.21, default_y=-21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=437.21, default_y=-17.5, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=479.4, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=521.6, default_y=-14.0, dynamics=70.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='44', width=502.76):
            with Note(default_x=10.0, default_y=-17.5, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=52.34, default_y=-17.5, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.09, default_y=-31.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.09, default_y=-21.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=162.43, default_y=-17.5, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=204.77, default_y=-17.5, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.11, default_y=-35.0, dynamics=56.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.45, default_y=-28.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=331.8, default_y=-42.0, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=374.14, default_y=-31.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=458.82, default_y=-42.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='45', width=348.1):
            with Note(default_x=12.66, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P8'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=174.78, default_y=0.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=206.77, default_y=10.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=238.77, default_y=-7.0, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=270.76, default_y=14.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=302.75, default_y=14.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=385.93, default_y=7.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=385.93, default_y=10.5, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=417.93, default_y=-7.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=449.92, default_y=14.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=398.1):
            with Note(default_x=10.0, default_y=14.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=96.63, default_y=7.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=96.63, default_y=10.5, dynamics=76.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=129.95, default_y=14.0, dynamics=52.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.59, default_y=3.5, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=229.91, default_y=-14.0, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=263.22, default_y=-17.5, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=296.54, default_y=-21.0, dynamics=55.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=329.86, default_y=17.5, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=363.18, default_y=14.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='3', width=502.62):
            with Note(default_x=10.94, default_y=14.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.53, default_y=-24.5, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.53, default_y=3.5, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=120.78, default_y=7.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=120.78, default_y=10.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=163.03, default_y=-38.5, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=205.28, default_y=-21.0, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.53, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=289.78, default_y=-24.5, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=332.02, default_y=7.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=374.27, default_y=-31.5, dynamics=62.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=416.52, default_y=-38.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=458.77, default_y=-21.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Time():
                    Beats('12')
                    BeatType('8')
            with Note(default_x=123.59, default_y=-42.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=154.47, default_y=-24.5, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=185.34, default_y=3.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=216.22, default_y=0.0, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=216.22, default_y=0.0, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=281.62, default_y=-3.5, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=312.49, default_y=-7.0, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=343.37, default_y=0.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=374.25, default_y=3.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=405.12, default_y=-49.0, dynamics=56.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=436.0, default_y=0.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=468.55, default_y=-3.5, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='5', width=459.0):
            with Note(default_x=17.26, default_y=-14.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=48.99, default_y=-31.5, dynamics=56.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=95.15, default_y=-28.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=138.95, default_y=-49.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.68, default_y=-17.5, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=216.84, default_y=-3.5, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=260.65, default_y=-7.0, dynamics=102.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=292.38, default_y=-35.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=324.11, default_y=-31.5, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=355.84, default_y=-52.5, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=387.57, default_y=3.5, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=456.22):
            with Note(default_x=17.8, default_y=7.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=53.98, default_y=0.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=90.15, default_y=7.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=126.33, default_y=7.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=198.68, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=234.85, default_y=3.5, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=307.2, default_y=-28.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.09, default_y=-3.5, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=418.44, default_y=0.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=0.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.62, default_y=0.0, dynamics=90.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.87, default_y=10.5, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=218.12, default_y=-7.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=253.38, default_y=14.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=288.63, default_y=14.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=380.29, default_y=7.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=380.29, default_y=10.5, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=415.54, default_y=-7.0, dynamics=62.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=450.8, default_y=14.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=403.82):
            with Note(default_x=10.0, default_y=14.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.91, default_y=7.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=97.91, default_y=10.5, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=131.72, default_y=14.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.35, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=233.16, default_y=-14.0, dynamics=53.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=266.97, default_y=-17.5, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=300.79, default_y=-21.0, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=334.6, default_y=17.5, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=368.41, default_y=14.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=524.78):
            with Note(default_x=10.94, default_y=14.0, dynamics=84.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.59, default_y=7.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=125.75, default_y=10.5, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=169.91, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=214.07, default_y=-21.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=258.23, default_y=-42.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=302.38, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=346.54, default_y=7.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=390.7, default_y=-31.5, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=434.86, default_y=-38.5, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=479.02, default_y=-21.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-42.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=149.56, default_y=-24.5, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.91, default_y=7.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=254.59, default_y=10.5, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=301.27, default_y=7.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=394.63, default_y=-21.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=452.97, default_y=10.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=512.61, default_y=14.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=559.29, default_y=17.5, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=605.97, default_y=10.5, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=10.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=79.38, default_y=10.5, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.37, default_y=7.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=133.37, default_y=10.5, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=187.36, default_y=7.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=241.34, default_y=10.5, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=295.33, default_y=7.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=349.31, default_y=3.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=403.3, default_y=7.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=470.78, default_y=3.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=524.77, default_y=0.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=592.25, default_y=7.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
            with Note(default_x=625.99, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=659.73, default_y=-31.5, dynamics=70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.32, default_y=-3.5, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=575.28, default_y=-3.5, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=802.9, default_y=-7.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=916.72, default_y=-31.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=1030.53, default_y=14.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=1144.34, default_y=14.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=1414.65, default_y=7.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=10.5, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=176.23, default_y=14.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=232.91, default_y=-14.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=261.24, default_y=-10.5, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=289.58, default_y=-28.0, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=317.92, default_y=0.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=346.26, default_y=3.5, dynamics=83.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=402.94, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='14', width=450.46):
            with Note(default_x=12.66, default_y=0.0, dynamics=82.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
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
            with Note(default_x=161.37, default_y=-14.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=201.02, default_y=0.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=240.68, default_y=-17.5, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=280.33, default_y=7.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=319.99, default_y=7.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=409.21, default_y=7.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='15', width=532.91):
            with Note(default_x=30.55, default_y=3.5, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.87, default_y=3.5, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=173.7, default_y=3.5, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=216.12, default_y=7.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=266.21, default_y=3.5, dynamics=91.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=308.62, default_y=3.5, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=393.46, default_y=3.5, dynamics=90.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=488.89, default_y=14.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-45.5, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.41, default_y=3.5, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=193.8, default_y=7.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=227.99, default_y=3.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=262.19, default_y=-3.5, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=296.38, default_y=-7.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=330.58, default_y=-35.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=364.77, default_y=-38.5, dynamics=53.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=398.97, default_y=7.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='17', width=375.51):
            with Note(default_x=23.55, default_y=3.5, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=112.56, default_y=0.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=201.57, default_y=3.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=249.05, default_y=0.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=249.05, default_y=-3.5, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=278.72, default_y=3.5, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=308.39, default_y=0.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=338.06, default_y=3.5, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='18', width=518.7):
            with Note(default_x=17.23, default_y=-3.5, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=164.03, default_y=-7.0, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=285.05, default_y=-7.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=401.07, default_y=-3.5, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=439.75, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=478.42, default_y=-10.5, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-10.5, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.4, default_y=-45.5, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.58, default_y=-49.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=265.76, default_y=10.5, dynamics=96.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=396.67, default_y=7.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=455.92, default_y=7.0, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=594.11, default_y=14.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=594.11, default_y=10.5, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=652.29, default_y=14.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=710.47, default_y=10.5, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='20', width=645.99):
            with Note(default_x=10.0, default_y=-17.5, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.69, default_y=7.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=119.38, default_y=3.5, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=174.07, default_y=3.5, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.76, default_y=-3.5, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=338.14, default_y=-7.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=480.33, default_y=-10.5, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=95.01, default_y=-14.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=140.24, default_y=-31.5, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=206.03, default_y=-24.5, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=271.82, default_y=0.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=443.51, default_y=3.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=488.74, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=554.53, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=615.2, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=660.43, default_y=-3.5, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=705.66, default_y=0.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='22', width=663.76):
            with Note(default_x=16.98, default_y=0.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=227.82, default_y=0.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=280.47, default_y=3.5, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=333.12, default_y=3.5, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=451.57, default_y=-3.5, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=504.22, default_y=-45.5, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=556.87, default_y=-28.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=609.51, default_y=10.5, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.81, default_y=7.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=137.65, default_y=3.5, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=169.92, default_y=0.0, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=202.19, default_y=-3.5, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=234.45, default_y=0.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=274.79, default_y=-3.5, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=324.85, default_y=-7.0, dynamics=57.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=397.46, default_y=-3.5, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=429.72, default_y=7.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=494.26, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=410.61):
            with Note(default_x=12.66, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
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
            with Note(default_x=146.98, default_y=7.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.8, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=218.62, default_y=-14.0, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=254.44, default_y=3.5, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=290.26, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=326.08, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=326.08, default_y=10.5, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=372.61, default_y=-3.5, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='25', width=477.52):
            with Note(default_x=13.8, default_y=0.0, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
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
            with Note(default_x=195.53, default_y=-24.5, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=231.87, default_y=0.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=277.31, default_y=-31.5, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=330.49, default_y=0.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=366.83, default_y=0.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=403.18, default_y=7.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=439.52, default_y=-31.5, dynamics=64.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-14.0, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=178.86, default_y=3.5, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=222.68, default_y=0.0, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=310.32, default_y=-3.5, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=354.14, default_y=0.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=518.48, default_y=0.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=0.0, dynamics=85.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=190.43, default_y=3.5, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=365.5, default_y=0.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=547.87, default_y=0.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=664.59, default_y=-42.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.32, default_y=0.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=240.14, default_y=0.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.29, default_y=-31.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=314.43, default_y=-28.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=351.57, default_y=-45.5, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=388.71, default_y=-42.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=425.85, default_y=-38.5, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=463.0, default_y=-42.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=509.42, default_y=-3.5, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='29', width=359.85):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=493.21):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=258.2, default_y=7.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.82, default_y=0.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=302.82, default_y=7.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=385.23, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=410.72, default_y=0.0, dynamics=63.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=440.62, default_y=-3.5, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=466.11, default_y=-7.0, dynamics=57.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=103.25, default_y=-3.5, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=212.54, default_y=10.5, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=267.19, default_y=10.5, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=321.84, default_y=7.0, dynamics=86.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=376.48, default_y=3.5, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=431.13, default_y=0.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=554.08, default_y=-3.5, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=608.73, default_y=0.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=663.37, default_y=0.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=676.14):
            with Note(default_x=10.0, default_y=0.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=58.91, default_y=-3.5, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.04, default_y=-7.0, dynamics=87.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=181.17, default_y=-10.5, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=230.08, default_y=-7.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=230.08, default_y=-3.5, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=352.35, default_y=-7.0, dynamics=81.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=625.63, default_y=-3.5, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=139.23, default_y=-17.5, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.26, default_y=3.5, dynamics=70.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=247.28, default_y=7.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=361.32, default_y=-10.5, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=361.32, default_y=7.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=505.38, default_y=7.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=3.5, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=199.66, default_y=7.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=343.12, default_y=3.5, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=553.02, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=670.39, default_y=3.5, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=95.37, default_y=-24.5, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.16, default_y=3.5, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=221.1, default_y=7.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=274.04, default_y=0.0, dynamics=78.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=340.21, default_y=-3.5, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=406.38, default_y=-7.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=472.55, default_y=0.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=525.49, default_y=3.5, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=578.43, default_y=7.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=684.3, default_y=3.5, dynamics=77.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='36', width=677.41):
            with Note(default_x=37.15, default_y=3.5, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=214.92, default_y=-3.5, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=280.76, default_y=-7.0, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=346.6, default_y=-10.5, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=412.44, default_y=-3.5, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=465.12, default_y=0.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=517.79, default_y=3.5, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=623.14, default_y=0.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=0.0, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=256.46, default_y=7.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
            with Note(default_x=430.75, default_y=3.5, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=596.0, default_y=0.0, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='38', width=644.36):
            with Note(default_x=19.16, default_y=3.5, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=141.31, default_y=0.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=308.46, default_y=-7.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=462.75, default_y=-7.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=514.18, default_y=7.0, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=618.11, default_y=-3.5, dynamics=91.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=668.38, default_y=-31.5, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=718.66, default_y=-35.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=645.72):
            with Note(default_x=10.0, default_y=0.0, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=115.69, default_y=-3.5, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=168.53, default_y=-14.0, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=327.06, default_y=-14.0, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
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
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
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
            with Note(default_x=249.76, default_y=-42.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=302.61, default_y=-35.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=355.46, default_y=-28.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=408.31, default_y=-31.5, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=461.16, default_y=-38.5, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=514.01, default_y=-21.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=566.86, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=619.71, default_y=3.5, dynamics=58.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=619.71, default_y=-24.5, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=672.56, default_y=7.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='42', width=689.24):
            with Note(default_x=13.8, default_y=-31.5, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=67.13, default_y=-38.5, dynamics=56.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.45, default_y=-45.5, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=173.78, default_y=0.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=227.1, default_y=3.5, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=227.1, default_y=-24.5, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=280.43, default_y=-28.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=367.69, default_y=-28.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=421.01, default_y=-31.5, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=474.34, default_y=-21.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=527.67, default_y=-24.5, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.21, default_y=-38.5, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=158.72, default_y=0.0, dynamics=81.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=200.92, default_y=10.5, dynamics=95.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=243.11, default_y=-7.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=285.31, default_y=14.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=327.5, default_y=21.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=437.21, default_y=7.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=437.21, default_y=17.5, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=479.4, default_y=-7.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=521.6, default_y=14.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='44', width=502.76):
            with Note(default_x=10.0, default_y=21.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=52.34, default_y=10.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.09, default_y=-7.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.09, default_y=10.5, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.43, default_y=21.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.77, default_y=17.5, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=247.11, default_y=0.0, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=331.8, default_y=-31.5, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=374.14, default_y=3.5, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=458.82, default_y=-3.5, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='45', width=348.1):
            with Note(default_x=12.66, default_y=-7.0, dynamics=58.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
            with Barline(location='right'):
                BarStyle('light-light')
    with Part(id='P9'):
        with Measure(number='1', width=483.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(120.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=174.78, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=206.77, default_y=-109.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=238.77, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=270.76, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=302.75, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=334.74, default_y=-113.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=385.93, default_y=-109.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=417.93, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=449.92, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=398.1):
            with Note(default_x=10.0, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=43.32, default_y=-113.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=96.63, default_y=-109.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=129.95, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=163.27, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=196.59, default_y=-116.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=229.91, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=263.22, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=296.54, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=329.86, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=363.18, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=502.62):
            with Note(default_x=10.94, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=163.03, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=205.28, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=247.53, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=289.78, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=332.02, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=374.27, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=416.52, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=458.77, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=501.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(605.72)
            with Attributes():
                with Time():
                    Beats('12')
                    BeatType('8')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=123.59, default_y=-623.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.47, default_y=-630.22):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=185.34, default_y=-609.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=216.22, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.1, default_y=-609.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=281.62, default_y=-605.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=312.49, default_y=-595.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=343.37, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=374.25, default_y=-609.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=405.12, default_y=-630.22):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=436.0, default_y=-598.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='5', width=459.0):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=17.26, default_y=-595.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.99, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.15, default_y=-609.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=138.95, default_y=-630.22):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=170.68, default_y=-598.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=260.65, default_y=-595.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=292.38, default_y=-616.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=324.11, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
            with Note(default_x=355.84, default_y=-633.72):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=387.57, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=422.1, default_y=-616.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=456.22):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=17.8, default_y=-637.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.15, default_y=-605.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=126.33, default_y=-595.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=162.5, default_y=-616.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=198.68, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=234.85, default_y=-633.72):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=271.03, default_y=-609.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=346.09, default_y=-605.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=382.27, default_y=-616.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=418.44, default_y=-612.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=487.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(149.14)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=91.21, default_y=-173.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=11.85, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=147.62, default_y=-149.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.87, default_y=-138.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=218.12, default_y=-156.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=253.38, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=288.63, default_y=-173.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=323.88, default_y=-142.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=380.29, default_y=-138.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=415.54, default_y=-156.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=450.8, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=403.82):
            with Note(default_x=10.0, default_y=-173.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=43.81, default_y=-142.14):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=97.91, default_y=-138.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=131.72, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.54, default_y=-149.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=199.35, default_y=-145.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=233.16, default_y=-163.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=266.97, default_y=-166.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=300.79, default_y=-170.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=334.6, default_y=-149.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=368.41, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=524.78):
            with Note(default_x=10.94, default_y=-173.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=169.91, default_y=-163.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=214.07, default_y=-170.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=258.23, default_y=-166.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=302.38, default_y=-173.64):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=346.54, default_y=-152.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=390.7, default_y=-156.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=434.86, default_y=-163.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=479.02, default_y=-170.14):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=700.93):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(598.92)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=91.21, default_y=-616.42):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.56, default_y=-623.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=207.91, default_y=-602.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=254.59, default_y=-605.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('2')
            with Note(default_x=301.27, default_y=-602.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=347.95, default_y=-598.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=394.63, default_y=-595.42):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=452.97, default_y=-605.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                    Suffix('flat')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=512.61, default_y=-602.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    Prefix('natural')
            with Note(default_x=559.29, default_y=-623.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=605.97, default_y=-605.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='11', width=715.32):
            with Note(default_x=25.4, default_y=-602.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=79.38, default_y=-609.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=133.37, default_y=-605.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=187.36, default_y=-623.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=241.34, default_y=-598.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=349.31, default_y=-595.42):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=403.3, default_y=-619.92):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=470.78, default_y=-616.42):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=524.77, default_y=-637.42):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=592.25, default_y=-605.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='12', width=1416.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(625.23)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=91.57, default_y=-628.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=205.39, default_y=-642.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=319.2, default_y=-639.23):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=433.01, default_y=-649.73):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=575.28, default_y=-618.23):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.7, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=802.9, default_y=-614.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=916.72, default_y=-632.23):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=1030.53, default_y=-628.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=1144.34, default_y=-649.73):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=1258.16, default_y=-618.23):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='13', width=432.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(132.43)
            with Note(default_x=91.21, default_y=-121.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.55, default_y=-139.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.89, default_y=-135.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.23, default_y=-142.93):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=204.57, default_y=-149.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.91, default_y=-146.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=261.24, default_y=-142.93):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=289.58, default_y=-160.43):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=317.92, default_y=-163.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=346.26, default_y=-167.43):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=374.6, default_y=-146.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=402.94, default_y=-149.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=450.46):
            with Note(default_x=12.66, default_y=-170.93):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=161.37, default_y=-146.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    Prefix('natural')
            with Note(default_x=201.02, default_y=-132.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=240.68, default_y=-149.93):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
            with Note(default_x=280.33, default_y=-146.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
            with Note(default_x=319.99, default_y=-170.93):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=359.64, default_y=-139.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='15', width=532.91):
            with Note(default_x=30.55, default_y=-135.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=88.87, default_y=-128.93):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=131.28, default_y=-118.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=173.7, default_y=-135.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                with Figure():
                    Prefix('natural')
            with Note(default_x=216.12, default_y=-132.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=266.21, default_y=-153.43):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=308.62, default_y=-121.93):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=393.46, default_y=-118.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=435.87, default_y=-135.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                with Figure():
                    Prefix('natural')
            with Note(default_x=488.89, default_y=-132.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=522.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(609.33)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=91.21, default_y=-630.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=125.41, default_y=-598.83):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('flat')
            with Note(default_x=193.8, default_y=-595.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=227.99, default_y=-612.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
                with Figure():
                    Prefix('natural')
            with Note(default_x=262.19, default_y=-609.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    Prefix('sharp')
            with Note(default_x=296.38, default_y=-605.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=330.58, default_y=-619.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=364.77, default_y=-623.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=398.97, default_y=-626.83):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=433.16, default_y=-605.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=475.91, default_y=-609.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=375.51):
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=23.55, default_y=-630.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.22, default_y=-633.83):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=82.89, default_y=-637.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=112.56, default_y=-640.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.23, default_y=-619.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=171.9, default_y=-623.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=201.57, default_y=-644.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=249.05, default_y=-619.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    Prefix('natural')
            with Note(default_x=278.72, default_y=-605.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=308.39, default_y=-616.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('backslash')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=338.06, default_y=-612.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=518.7):
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=17.23, default_y=-633.83):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=55.91, default_y=-609.33):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=164.03, default_y=-605.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=202.71, default_y=-626.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=241.38, default_y=-623.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=285.05, default_y=-640.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=323.73, default_y=-633.83):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            FiguredBass()
            with Note(default_x=362.4, default_y=-630.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=401.07, default_y=-626.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=439.75, default_y=-623.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=478.42, default_y=-619.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=770.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(602.08)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    Prefix('sharp')
            with Note(default_x=91.21, default_y=-609.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=149.4, default_y=-623.08):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=207.58, default_y=-626.58):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=265.76, default_y=-630.08):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=338.49, default_y=-609.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=396.67, default_y=-612.58):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=455.92, default_y=-633.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    Extend(type='stop')
            with Note(default_x=514.1, default_y=-609.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('backslash')
            with Note(default_x=594.11, default_y=-605.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=652.29, default_y=-626.58):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=710.47, default_y=-623.08):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=645.99):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=10.0, default_y=-619.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=64.69, default_y=-637.08):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=119.38, default_y=-640.58):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=174.07, default_y=-644.08):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=228.76, default_y=-623.08):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=283.45, default_y=-626.58):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=338.14, default_y=-623.08):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=589.71, default_y=-602.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='21', width=752.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(637.54)
            with Note(default_x=95.01, default_y=-627.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=140.24, default_y=-644.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.03, default_y=-637.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=271.82, default_y=-651.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=317.05, default_y=-627.04):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('flat')
            with Note(default_x=443.51, default_y=-623.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=488.74, default_y=-644.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=554.53, default_y=-641.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=615.2, default_y=-648.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=660.43, default_y=-630.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='22', width=663.76):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=17.23, default_y=-627.04):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.88, default_y=-637.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.53, default_y=-634.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=175.17, default_y=-651.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=227.82, default_y=-627.04):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=333.12, default_y=-623.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=398.93, default_y=-651.54):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=451.57, default_y=-648.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=504.22, default_y=-655.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                Duration(4.0)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
                Duration(4.0)
            with Note(default_x=556.87, default_y=-641.04):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='23', width=528.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(126.56)
            with FiguredBass():
                with Figure():
                    Prefix('natural')
            with Note(default_x=103.81, default_y=-126.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=234.45, default_y=-140.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=274.79, default_y=-137.06):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=324.85, default_y=-133.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=365.19, default_y=-151.06):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=397.46, default_y=-154.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=429.72, default_y=-158.06):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=461.99, default_y=-137.06):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=494.26, default_y=-140.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=410.61):
            with Note(default_x=12.66, default_y=-161.56):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=146.98, default_y=-137.06):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.8, default_y=-123.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=218.62, default_y=-140.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=254.44, default_y=-137.06):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=290.26, default_y=-161.56):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=326.08, default_y=-130.06):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='25', width=477.52):
            with Note(default_x=13.8, default_y=-126.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
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
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=195.53, default_y=-126.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=231.87, default_y=-116.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=277.31, default_y=-133.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                    Suffix('flat')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=330.49, default_y=-130.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    Prefix('natural')
            with Note(default_x=366.83, default_y=-151.06):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=403.18, default_y=-133.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='26', width=684.41):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(605.19)
            with Note(default_x=91.21, default_y=-608.69):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=135.03, default_y=-612.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=178.86, default_y=-608.69):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=222.68, default_y=-605.19):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=266.5, default_y=-619.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=310.32, default_y=-615.69):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=354.14, default_y=-612.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=408.92, default_y=-622.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=463.7, default_y=-619.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=518.48, default_y=-629.69):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=573.25, default_y=-598.19):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='27', width=731.84):
            with Note(default_x=15.35, default_y=-594.69):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.71, default_y=-612.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=132.07, default_y=-608.69):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=190.43, default_y=-615.69):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=248.79, default_y=-598.19):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=365.5, default_y=-594.69):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=423.86, default_y=-612.19):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=482.22, default_y=-608.69):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=547.87, default_y=-629.69):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=606.23, default_y=-622.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='28', width=563.19):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(600.79)
            with Note(default_x=91.57, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=128.72, default_y=-632.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.86, default_y=-625.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.0, default_y=-639.29):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                Duration(4.0)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
                Duration(4.0)
            with Note(default_x=240.14, default_y=-607.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=314.43, default_y=-604.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=351.57, default_y=-621.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass(parentheses='yes'):
                with Figure():
                    FigureNumber('6')
            with Note(default_x=388.71, default_y=-618.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=425.85, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=463.0, default_y=-618.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=509.42, default_y=-621.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=359.85):
            with Note(default_x=13.8, default_y=-625.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=41.91, default_y=-593.79):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=70.01, default_y=-590.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.12, default_y=-586.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.23, default_y=-600.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.33, default_y=-604.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=182.44, default_y=-607.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=210.54, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=245.83, default_y=-611.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
            with Note(default_x=273.93, default_y=-607.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=302.04, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=330.14, default_y=-618.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=493.21):
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=19.97, default_y=-621.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=55.03, default_y=-618.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=106.01, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    Prefix('sharp')
            with Note(default_x=153.04, default_y=-611.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=188.09, default_y=-614.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=223.15, default_y=-611.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=258.2, default_y=-625.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=440.62, default_y=-625.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='31', width=740.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(129.48)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                    Suffix('cross')
                with Figure():
                    FigureNumber('2')
                    Suffix('cross')
            with Note(default_x=103.25, default_y=-143.48):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=157.9, default_y=-157.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.54, default_y=-150.48):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
            with Note(default_x=267.19, default_y=-164.48):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=321.84, default_y=-139.98):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=431.13, default_y=-136.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=485.77, default_y=-153.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=554.08, default_y=-146.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=608.73, default_y=-160.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=663.37, default_y=-143.48):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='32', width=676.14):
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
            with Note(default_x=10.0, default_y=-139.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=58.91, default_y=-157.48):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.04, default_y=-150.48):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=181.17, default_y=-164.48):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=230.08, default_y=-146.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=352.35, default_y=-143.48):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    Prefix('sharp')
            with Note(default_x=625.63, default_y=-139.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='33', width=663.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(615.26)
            with Note(default_x=91.21, default_y=-615.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.23, default_y=-632.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('sharp')
            with Note(default_x=199.26, default_y=-625.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Prefix('natural')
            with Note(default_x=247.28, default_y=-639.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('flat')
            with Note(default_x=295.3, default_y=-625.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
                    Extend(type='start')
            with Note(default_x=361.32, default_y=-622.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    Extend(type='stop')
                with Figure():
                    Extend(type='continue')
            with Note(default_x=409.34, default_y=-646.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    Extend(type='stop')
                with Figure():
                    Extend(type='continue')
            with Note(default_x=457.36, default_y=-639.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    Extend(type='stop')
                with Figure():
                    Extend(type='stop')
            with Note(default_x=505.38, default_y=-653.76):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=553.4, default_y=-622.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='34', width=753.2):
            with Note(default_x=18.14, default_y=-618.76):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=65.96, default_y=-629.26):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=135.52, default_y=-625.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=199.66, default_y=-639.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=247.48, default_y=-615.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=343.12, default_y=-611.76):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=390.93, default_y=-636.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=460.49, default_y=-632.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=553.02, default_y=-653.76):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=600.84, default_y=-615.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=670.39, default_y=-618.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=738.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(599.34)
            with Note(default_x=95.37, default_y=-623.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=274.04, default_y=-613.34):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=340.21, default_y=-609.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('backslash')
            with Note(default_x=406.38, default_y=-606.34):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=472.55, default_y=-623.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=525.49, default_y=-627.34):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=578.43, default_y=-630.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=631.37, default_y=-609.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=684.3, default_y=-613.34):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=677.41):
            with Note(default_x=37.15, default_y=-634.34):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=214.92, default_y=-616.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=280.76, default_y=-613.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=346.6, default_y=-609.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=412.44, default_y=-627.34):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=465.12, default_y=-630.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=517.79, default_y=-634.34):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=570.46, default_y=-613.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=623.14, default_y=-616.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=771.89):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(622.54)
            with Note(default_x=91.21, default_y=-636.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=198.36, default_y=-622.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
            with Note(default_x=256.46, default_y=-612.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                    Suffix('natural')
            with Note(default_x=314.56, default_y=-626.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=372.65, default_y=-626.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=430.75, default_y=-643.54):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=488.85, default_y=-615.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with FiguredBass():
                with Figure():
                    FigureNumber('2')
                    Extend(type='start')
            with Note(default_x=596.0, default_y=-612.04):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    Extend(type='continue')
            with Note(default_x=654.09, default_y=-633.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    Extend(type='continue')
            with Note(default_x=712.19, default_y=-629.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='38', width=644.36):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=19.16, default_y=-650.54):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=70.59, default_y=-626.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=141.31, default_y=-622.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=192.74, default_y=-647.04):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=257.03, default_y=-643.54):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=308.46, default_y=-640.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=359.89, default_y=-657.54):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=411.32, default_y=-654.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=462.75, default_y=-661.04):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=514.18, default_y=-629.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='39', width=770.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(136.37)
            with Note(default_x=91.21, default_y=-139.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
            with Note(default_x=141.49, default_y=-146.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=191.76, default_y=-143.37):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=242.04, default_y=-139.87):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=304.88, default_y=-153.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=367.72, default_y=-157.37):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=430.56, default_y=-160.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=493.41, default_y=-136.37):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=567.83, default_y=-132.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=618.11, default_y=-129.37):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=668.38, default_y=-143.37):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=718.66, default_y=-146.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=645.72):
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                    Suffix('flat')
            with Note(default_x=10.0, default_y=-150.37):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.84, default_y=-150.37):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=115.69, default_y=-146.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
                    Suffix('flat')
            with Note(default_x=168.53, default_y=-143.37):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=221.37, default_y=-157.37):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    Prefix('natural')
            with Note(default_x=274.22, default_y=-160.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=327.06, default_y=-164.37):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='41', width=727.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(120.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=249.76, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=302.61, default_y=-130.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=355.46, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=408.31, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=461.16, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=514.01, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=566.86, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
            with Note(default_x=619.71, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=672.56, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=689.24):
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=13.8, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.13, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=120.45, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=173.78, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=227.1, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=280.43, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=367.69, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=421.01, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=474.34, default_y=-116.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('7')
                Duration(4.0)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                Duration(4.0)
            with Note(default_x=527.67, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
            with Note(default_x=634.32, default_y=-144.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='43', width=565.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(120.0)
            with Note(default_x=91.21, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=158.72, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=200.92, default_y=-109.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.11, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=285.31, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=327.5, default_y=-130.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=369.7, default_y=-113.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=437.21, default_y=-109.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=479.4, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=521.6, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='44', width=502.76):
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=10.0, default_y=-130.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=52.34, default_y=-127.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=120.09, default_y=-123.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('5')
            with Note(default_x=162.43, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('2')
            with Note(default_x=204.77, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=247.11, default_y=-130.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('4')
                with Figure():
                    FigureNumber('2')
            with Note(default_x=289.45, default_y=-148.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=331.8, default_y=-151.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with FiguredBass(parentheses='yes'):
                with Figure():
                    FigureNumber('7')
            with Note(default_x=374.14, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=416.48, default_y=-134.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('3')
            with Note(default_x=458.82, default_y=-137.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='45', width=348.1):
            with Note(default_x=12.66, default_y=-158.5):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-light')