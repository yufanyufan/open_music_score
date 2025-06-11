with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Title')
    with Identification():
        Creator('Composer', type='composer')
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
        CreditWords('Wer ein liebchen hat gefunden', default_x=671.547, default_y=1834.59, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Mozart', default_x=1279.15, default_y=1734.59, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Bas')
            PartAbbreviation('Bs.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Bas')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(43)
                Volume(34.6457)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(96.8504)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=179.39):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(84.98)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-35.88, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=183.88):
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('1')
        with Measure(number='3', width=176.95):
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
            with Note(default_x=108.84, default_y=-20.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wer')
            with Note(default_x=143.82, default_y=-20.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
        with Measure(number='4', width=203.06):
            with Note(default_x=25.72, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=78.82, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=115.16, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=168.27, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='5', width=179.53):
            with Note(default_x=21.03, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.13, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=47.18, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=73.33, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=125.63, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=151.78, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='6', width=207.42):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=15.8, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=49.73, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=83.67, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=117.6, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('red')
            with Note(default_x=171.89, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='7', width=258.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(137.66)
            with Note(default_x=92.58, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('meint')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=190.27, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('lohn')
            with Note(default_x=223.37, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='8', width=250.48):
            with Note(default_x=12.0, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ihr')
            with Note(default_x=54.3, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.6, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('durch')
            with Note(default_x=138.9, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tau')
            with Note(default_x=206.58, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('send')
        with Measure(number='9', width=227.7):
            with Note(default_x=22.56, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Küs')
            with Note(default_x=79.54, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.77, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mach')
            with Note(default_x=190.48, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='10', width=199.12):
            with Note(default_x=12.0, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('all')
            with Note(default_x=45.13, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=78.26, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('das')
            with Note(default_x=111.39, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=164.39, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='11', width=207.04):
            with Note(default_x=17.23, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=71.0, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.22, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sei')
            with Note(default_x=171.83, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='12', width=434.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(137.66)
            with Note(default_x=92.58, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tröst')
            with Note(default_x=149.36, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=206.14, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=262.92, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=376.48, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='13', width=357.13):
            with Note(default_x=36.69, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.92, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=3.67, relative_y=41.22):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=249.25, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=302.39, default_y=-20.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='14', width=350.42):
            with Note(default_x=15.8, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Trö')
            with Note(default_x=67.48, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=119.16, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=170.84, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=278.26, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='15', width=233.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(-0.0)
                    SystemDistance(137.66)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=92.58, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.92, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=150.88, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=198.7, default_y=-35.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='16', width=174.07):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note(default_x=36.77, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=97.16, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tral')
            with Note(default_x=143.99, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='17', width=168.52):
            with Note(default_x=15.8, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=40.33, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=64.86, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=89.38, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=113.91, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=138.44, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='18', width=146.11):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=50.02, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=77.52, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=111.74, default_y=15.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='19', width=263.78):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=15.8, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=48.71, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=81.61, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=114.52, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=147.43, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=163.09, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.76, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.42, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=211.85, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=229.28, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
        with Measure(number='20', width=156.86):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=5.26, relative_y=38.5):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=89.04, default_y=-20.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Doch')
            with Note(default_x=126.95, default_y=-20.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
        with Measure(number='21', width=301.92):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=88.9, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=159.37, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich')
            with Note(default_x=194.61, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=265.08, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='22', width=271.29):
            with Note(default_x=17.23, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('hal')
            with Note(default_x=58.11, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=98.99, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.94, default_y=-46.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.76, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.6, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text("schliess'")
            with Note(default_x=228.81, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=337.61):
            with Note(default_x=25.72, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=77.43, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chen')
            with Note(default_x=129.15, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=180.86, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sorg')
            with Note(default_x=284.29, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='24', width=231.59):
            with Note(default_x=18.34, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein;')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.41, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=194.97, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='25', width=347.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=88.9, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lo')
            with Note(default_x=128.38, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=167.87, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen')
            with Note(default_x=217.51, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ding')
            with Note(default_x=303.41, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
        with Measure(number='26', width=245.8):
            with Note(default_x=15.79, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=90.43, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('schen')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.06, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
            with Note(default_x=202.38, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='27', width=285.08):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=12.12, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmet')
            with Note(default_x=54.7, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.29, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=148.48, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling')
            with Note(default_x=239.03, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='28', width=263.61):
            with Note(default_x=17.23, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=104.64, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('schen')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=181.33, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=219.67, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='29', width=341.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=88.9, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=130.24, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=171.59, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=212.93, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Note(default_x=295.62, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='30', width=274.46):
            with Note(default_x=29.33, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=189.59, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=229.66, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='31', width=284.33):
            with Note(default_x=15.8, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=58.57, default_y=10.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=101.35, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=144.12, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=238.18, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='32', width=242.56):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=29.26, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.91, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
            with Note(default_x=106.42, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=146.37, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=205.66, default_y=-35.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='33', width=259.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=88.78, default_y=-40.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=161.26, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=220.7, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='34', width=223.02):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=15.8, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=50.07, default_y=10.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.34, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=118.61, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=152.88, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('630')
                Sound(tempo=630.0)
            with Note(default_x=187.15, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='35', width=198.09):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=71.4, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=106.15, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=161.75, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='36', width=253.14):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=17.23, default_y=15.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=56.28, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=95.34, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=134.39, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=173.44, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=212.49, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
        with Measure(number='37', width=208.7):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Sound(tempo=50.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=129.82, default_y=-20.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Son')
            with Note(default_x=168.46, default_y=-20.0, dynamics=85.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
        with Measure(number='38', width=419.89):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=92.58, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=203.15, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('beim')
            with Note(default_x=256.94, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mon')
            with Note(default_x=364.51, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='39', width=340.68):
            with Note(default_x=17.23, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schei')
            with Note(default_x=70.87, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.52, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.91, default_y=-43.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freun')
            with Note(default_x=285.44, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.02, default_y=-43.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='40', width=381.84):
            with Note(default_x=15.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('nehmt')
                    Extend()
            with Note(default_x=76.54, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.28, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=198.02, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl')
            with Note(default_x=319.5, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
        with Measure(number='41', width=332.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=88.78, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('acht')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=21.24, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('135')
                Sound(tempo=135.0)
            with Direction():
                with DirectionType():
                    Words('Allegro', relative_y=20.0)
            with Note(default_x=238.38, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=283.97, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('lauscht')
        with Measure(number='42', width=176.36):
            with Note(default_x=12.0, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                    Extend()
            with Note(default_x=40.26, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=68.51, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Note(default_x=98.98, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('jun')
            with Note(default_x=144.2, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges')
        with Measure(number='43', width=225.03):
            with Note(default_x=25.94, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Herr')
            with Note(default_x=81.29, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.47, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('kirrt')
            with Note(default_x=188.84, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='44', width=194.48):
            with Note(default_x=12.0, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('lockt')
                    Extend()
            with Note(default_x=45.54, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.38, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=110.11, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('klei')
            with Note(default_x=161.04, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='45', width=213.72):
            with Note(default_x=17.23, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Närr')
            with Note(default_x=69.7, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=21.24, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Sound(tempo=50.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction():
                with DirectionType():
                    Words('A tempo', relative_y=20.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=21.24, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=135.29, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=174.79, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='46', width=339.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=88.9, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Note(default_x=129.98, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=171.06, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=212.14, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=294.3, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='47', width=288.99):
            with Note(default_x=31.77, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=200.83, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=243.09, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='48', width=302.12):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=2.72, relative_y=37.28):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=15.8, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=58.76, default_y=10.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=101.71, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=144.67, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=230.59, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='49', width=211.7):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=31.81, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Note(default_x=126.71, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=177.32, default_y=-35.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='50', width=242.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note(default_x=89.72, default_y=-40.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=154.5, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=207.63, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='51', width=211.66):
            with Note(default_x=15.8, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=48.18, default_y=10.0, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=80.55, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=112.93, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-40.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=145.31, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=177.69, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='52', width=171.72):
            with Note(default_x=13.09, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=61.06, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=92.16, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=140.13, default_y=15.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='53', width=392.88):
            with Note(default_x=14.0, default_y=15.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=55.76, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-40.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=96.64, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=137.51, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-40.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
                    Extend()
            with Note(default_x=157.2, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=176.9, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.59, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('forward hook', number=4)
            with Note(default_x=216.06, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(45.0)
                Voice('1')
                Type('32nd')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=245.33, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=350.41, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('le')
        with Measure(number='54', width=123.72):
            with Note(default_x=14.21, default_y=-5.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ra')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=179.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(78.08)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=109.66, default_y=-128.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=145.02, default_y=-128.08):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=109.66, default_y=-163.08, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=109.66, default_y=-148.08, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=109.66, default_y=-253.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='2', width=183.88):
            with Note(default_x=12.0, default_y=-128.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.08, default_y=-133.08, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.15, default_y=-138.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.05, default_y=-163.08, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.05, default_y=-153.08, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=98.05, default_y=-138.08, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=126.13, default_y=-168.08, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.13, default_y=-143.08, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=154.21, default_y=-173.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.21, default_y=-148.08, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-158.08, dynamics=51.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-148.08, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=12.0, default_y=-248.08, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=98.05, default_y=-243.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='3', width=176.95):
            with Note(default_x=15.8, default_y=-173.08, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-163.08, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-148.08, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=77.31, default_y=-173.08, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.31, default_y=-163.08, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.31, default_y=-148.08, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-263.08, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=77.31, default_y=-263.08, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='4', width=203.06):
            with Note(default_x=25.72, default_y=-173.08, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=25.72, default_y=-163.08, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.72, default_y=-148.08, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.16, default_y=-173.08, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.16, default_y=-163.08, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.16, default_y=-148.08, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=25.72, default_y=-263.08, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.16, default_y=-253.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='5', width=179.53):
            with Note(default_x=21.03, default_y=-178.08, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-163.08, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-153.08, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=99.48, default_y=-163.08, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.48, default_y=-148.08, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=99.48, default_y=-138.08, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=21.03, default_y=-243.08, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.48, default_y=-253.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='6', width=207.42):
            with Note(default_x=15.8, default_y=-138.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.73, default_y=-143.08, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.67, default_y=-148.08, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.6, default_y=-148.08, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=171.89, default_y=-153.08, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-168.08, dynamics=51.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-158.08, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=105.73, default_y=-168.08, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=117.6, default_y=-163.08, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-248.08, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.6, default_y=-243.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='7', width=258.07):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.44)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=92.58, default_y=-166.44, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.58, default_y=-156.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=92.58, default_y=-141.44, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=157.16, default_y=-156.44, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.16, default_y=-141.44, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=157.16, default_y=-131.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=92.58, default_y=-256.44, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.16, default_y=-221.44, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='8', width=250.48):
            with Note(default_x=12.0, default_y=-156.44, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-146.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-136.44, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=138.9, default_y=-151.44, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.9, default_y=-141.44, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=150.77, default_y=-136.44, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-236.44, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.9, default_y=-241.44, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=227.7):
            with Note(default_x=22.56, default_y=-156.44, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=22.56, default_y=-146.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=22.56, default_y=-136.44, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.15, default_y=-156.44, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.15, default_y=-141.44, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.15, default_y=-131.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=22.56, default_y=-236.44, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.15, default_y=-221.44, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='10', width=199.12):
            with Note(default_x=12.0, default_y=-156.44, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-146.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-136.44, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=111.39, default_y=-151.44, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=111.39, default_y=-141.44, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=123.25, default_y=-136.44, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-236.44, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=111.39, default_y=-241.44, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=207.04):
            with Note(default_x=17.23, default_y=-156.44, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-146.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-136.44, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=104.61, default_y=-181.44, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.61, default_y=-171.44, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=104.61, default_y=-156.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-236.44, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.61, default_y=-271.44, dynamics=53.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=434.86):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.95)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=92.58, default_y=-173.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.97, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.36, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.75, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.14, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.53, default_y=-163.95, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=262.92, default_y=-168.95, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.31, default_y=-158.95, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.7, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.09, default_y=-158.95, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.48, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=404.87, default_y=-158.95, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=92.58, default_y=-253.95, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=262.92, default_y=-268.95, dynamics=53.33):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=357.13):
            with Note(default_x=36.69, default_y=-173.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=63.26, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.83, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.4, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.97, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.54, default_y=-163.95, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.11, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.68, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.25, default_y=-138.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.82, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.39, default_y=-138.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.96, default_y=-153.95, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=36.69, default_y=-253.95, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=196.11, default_y=-253.95, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=350.42):
            with Note(default_x=15.8, default_y=-163.95, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.64, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.48, default_y=-138.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.32, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.16, default_y=-138.95, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.0, default_y=-153.95, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=170.84, default_y=-158.95, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.68, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.58, default_y=-143.95, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.42, default_y=-153.95, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.26, default_y=-143.95, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.1, default_y=-153.95, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-218.95, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=170.84, default_y=-233.95, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='15', width=233.07):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.28)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=92.58, default_y=-190.28, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.58, default_y=-165.28, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=150.88, default_y=-145.28, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=150.88, default_y=-130.28, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=150.88, default_y=-120.28, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=198.7, default_y=-150.28, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=198.7, default_y=-135.28, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=198.7, default_y=-125.28, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=92.58, default_y=-280.28, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=150.88, default_y=-225.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='16', width=174.07):
            with Note(default_x=36.77, default_y=-155.28, dynamics=40.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=36.77, default_y=-130.28, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=120.86, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.99, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=97.16, default_y=-180.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=36.77, default_y=-210.28, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=97.16, default_y=-245.28, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=168.52):
            with Note(default_x=15.8, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.33, default_y=-150.28, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.86, default_y=-155.28, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=89.38, default_y=-155.28, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.91, default_y=-160.28, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.44, default_y=-190.28, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.44, default_y=-165.28, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-175.28, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=89.38, default_y=-180.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-245.28, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.38, default_y=-250.28, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=138.44, default_y=-245.28, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=146.11):
            with Note(default_x=15.8, default_y=-190.28, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-165.28, dynamics=60.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=77.52, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=111.74, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=77.52, default_y=-180.28, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=77.52, default_y=-165.28, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-245.28, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=77.52, default_y=-270.28, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='19', width=263.78):
            with Note(default_x=20.1, default_y=-145.28, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.71, default_y=-150.28, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.61, default_y=-155.28, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.52, default_y=-170.28, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=114.52, default_y=-155.28, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=147.43, default_y=-160.28, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.28, default_y=-165.28, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-165.28, dynamics=52.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(360.0)
            with Note(default_x=20.1, default_y=-175.28, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.52, default_y=-185.28, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-265.28, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=114.52, default_y=-260.28, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='20', width=156.86):
            with Note(default_x=15.8, default_y=-190.28, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-180.28, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-165.28, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=64.22, default_y=-190.28, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.22, default_y=-180.28, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.22, default_y=-165.28, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-245.28, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=64.22, default_y=-245.28, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='21', width=301.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.08)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.13, default_y=-142.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.37, default_y=-127.08, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=229.85, default_y=-117.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=265.08, default_y=-127.08, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=88.9, default_y=-232.08, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.61, default_y=-227.08, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=271.29):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=58.11, default_y=-132.08, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.99, default_y=-122.08, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=180.76, default_y=-107.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=228.81, default_y=-117.08, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-222.08, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=139.88, default_y=-242.08, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='23', width=337.61):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=77.43, default_y=-122.08, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.15, default_y=-112.08, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=232.58, default_y=-142.08, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=284.29, default_y=-132.08, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=25.72, default_y=-237.08, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=180.86, default_y=-227.08, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='24', width=231.59):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.36, default_y=-127.08, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.38, default_y=-142.08, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=158.41, default_y=-152.08, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=194.97, default_y=-162.08, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.34, default_y=-232.08, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.4, default_y=-242.08, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='25', width=347.92):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.38, default_y=-124.2, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=167.87, default_y=-119.2, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=263.92, default_y=-114.2, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.41, default_y=-119.2, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=88.9, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.64, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.38, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.13, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.87, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.62, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=217.51, default_y=-259.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=244.18, default_y=-249.2, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.92, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.67, default_y=-249.2, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.41, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.16, default_y=-249.2, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=245.8):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.11, default_y=-109.2, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.43, default_y=-104.2, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=165.06, default_y=-179.2, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.38, default_y=-174.2, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.79, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.45, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.11, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.77, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.43, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.09, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.74, default_y=-274.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.4, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.06, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.72, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.38, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.04, default_y=-239.2, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=285.08):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=54.7, default_y=-124.2, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.29, default_y=-119.2, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=196.44, default_y=-114.2, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=239.03, default_y=-119.2, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.41, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.7, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.0, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.29, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.58, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.48, default_y=-259.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.15, default_y=-249.2, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.44, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.73, default_y=-249.2, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.03, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.32, default_y=-249.2, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=263.61):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=66.3, default_y=-109.2, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=104.64, default_y=-104.2, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=181.33, default_y=-179.2, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=219.67, default_y=-174.2, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.13, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.3, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.47, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.64, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.81, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.98, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.16, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.33, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.5, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.67, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.84, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=341.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=130.24, default_y=-139.2, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.59, default_y=-124.2, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=254.28, default_y=-124.2, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=295.62, default_y=-129.2, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=88.9, default_y=-274.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.57, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.24, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.91, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.59, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.26, default_y=-239.2, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.93, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.6, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.28, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.95, default_y=-234.2, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.62, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.29, default_y=-234.2, dynamics=35.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=274.46):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.39, default_y=-124.2, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.46, default_y=-114.2, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=189.59, default_y=-114.2, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=229.66, default_y=-104.2, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=29.33, default_y=-264.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.36, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.39, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.43, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.46, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.49, default_y=-254.2, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.53, default_y=-274.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.56, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.59, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.63, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.66, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.7, default_y=-254.2, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=284.33):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=58.57, default_y=-139.2, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.35, default_y=-114.2, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=195.4, default_y=-114.2, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.18, default_y=-119.2, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-274.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.19, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.57, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.96, default_y=-239.2, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.35, default_y=-229.2, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.73, default_y=-239.2, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.12, default_y=-254.2, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.02, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.4, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.79, default_y=-244.2, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.18, default_y=-224.2, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.56, default_y=-244.2, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=242.56):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=58.65, default_y=-124.2, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.05, default_y=-149.2, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.76, default_y=-139.2, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=205.66, default_y=-164.2, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=29.26, default_y=-229.2, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=146.37, default_y=-219.2, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=205.66, default_y=-224.2, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=259.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(98.44)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.78, default_y=-168.44, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=161.26, default_y=-148.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=220.7, default_y=-148.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=161.26, default_y=-183.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=88.78, default_y=-238.44, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=161.26, default_y=-248.44, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=223.02):
            with Note(default_x=15.8, default_y=-148.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.07, default_y=-153.44, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=84.34, default_y=-158.44, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.61, default_y=-183.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.61, default_y=-158.44, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.88, default_y=-188.44, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.88, default_y=-163.44, dynamics=48.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=187.15, default_y=-193.44, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=187.15, default_y=-168.44, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-178.44, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=15.8, default_y=-248.44, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.61, default_y=-253.44, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=187.15, default_y=-248.44, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=198.09):
            with Note(default_x=15.8, default_y=-193.44, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-168.44, dynamics=60.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=106.15, default_y=-148.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=161.75, default_y=-148.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=94.28, default_y=-173.44, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=106.15, default_y=-168.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-248.44, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=106.15, default_y=-273.44, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=253.14):
            with Note(default_x=17.23, default_y=-168.44, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-148.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=56.28, default_y=-153.44, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.34, default_y=-168.44, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.34, default_y=-158.44, dynamics=56.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=134.39, default_y=-183.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.39, default_y=-168.44, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=134.39, default_y=-158.44, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.44, default_y=-188.44, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=173.44, default_y=-173.44, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=173.44, default_y=-163.44, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=212.49, default_y=-193.44, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=212.49, default_y=-168.44, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-178.44, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=17.23, default_y=-268.44, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=134.39, default_y=-263.44, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='37', width=208.7):
            with Note(default_x=15.8, default_y=-193.44, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-183.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=-168.44, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.18, default_y=-193.44, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=91.18, default_y=-183.44, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=91.18, default_y=-168.44, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-248.44, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Staccato()
            with Note(default_x=91.18, default_y=-248.44, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='38', width=419.89):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.33)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=92.58, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.47, default_y=-134.33, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.37, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.26, default_y=-124.33, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.15, default_y=-119.33, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.04, default_y=-124.33, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=256.94, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.83, default_y=-134.33, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.72, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.61, default_y=-124.33, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.51, default_y=-119.33, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.4, default_y=-129.33, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=92.58, default_y=-224.33, dynamics=66.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=256.94, default_y=-234.33, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='39', width=340.68):
            with Note(default_x=17.23, default_y=-134.33, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.05, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.87, default_y=-124.33, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.69, default_y=-144.33, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.52, default_y=-139.33, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.34, default_y=-134.33, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.16, default_y=-129.33, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.98, default_y=-124.33, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.8, default_y=-119.33, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.62, default_y=-114.33, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.44, default_y=-109.33, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.26, default_y=-119.33, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-239.33, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=178.16, default_y=-244.33, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='40', width=381.84):
            with Note(default_x=15.8, default_y=-124.33, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.17, default_y=-119.33, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.54, default_y=-114.33, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.91, default_y=-109.33, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.28, default_y=-104.33, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.65, default_y=-114.33, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.02, default_y=-119.33, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.39, default_y=-114.33, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.76, default_y=-109.33, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.13, default_y=-144.33, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.5, default_y=-139.33, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.87, default_y=-134.33, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-239.33, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=198.02, default_y=-234.33, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=319.5, default_y=-229.33, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=332.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.95)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.78, default_y=-110.95, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.46, default_y=-120.95, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.15, default_y=-125.95, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.83, default_y=-130.95, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.52, default_y=-135.95, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.2, default_y=-140.95, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=206.89, default_y=-145.95, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=88.78, default_y=-215.95, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=206.89, default_y=-205.95, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='42', width=176.36):
            with Note(default_x=12.0, default_y=-160.95, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-150.95, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-140.95, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=98.98, default_y=-155.95, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.98, default_y=-145.95, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=110.85, default_y=-140.95, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-240.95, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.98, default_y=-245.95, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=225.03):
            with Note(default_x=25.94, default_y=-160.95, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=25.94, default_y=-150.95, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.94, default_y=-140.95, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.88, default_y=-160.95, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.88, default_y=-145.95, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.88, default_y=-135.95, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=25.94, default_y=-240.95, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.88, default_y=-225.95, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='44', width=194.48):
            with Note(default_x=12.0, default_y=-160.95, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-150.95, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-140.95, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=110.11, default_y=-155.95, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.11, default_y=-145.95, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=121.97, default_y=-140.95, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-240.95, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.11, default_y=-245.95, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=213.72):
            with Note(default_x=17.23, default_y=-160.95, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-150.95, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-140.95, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-240.95, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='46', width=339.61):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.71)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=129.98, default_y=-178.71, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.06, default_y=-163.71, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=253.22, default_y=-163.71, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=294.3, default_y=-168.71, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=88.9, default_y=-278.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.44, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.98, default_y=-233.71, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.52, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.06, default_y=-233.71, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.6, default_y=-243.71, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.14, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.68, default_y=-238.71, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.22, default_y=-228.71, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.76, default_y=-238.71, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.3, default_y=-228.71, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.84, default_y=-238.71, dynamics=35.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=288.99):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=74.03, default_y=-163.71, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=116.3, default_y=-153.71, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=200.83, default_y=-153.71, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=243.09, default_y=-143.71, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.77, default_y=-268.71, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.9, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.03, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.17, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.3, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.43, default_y=-258.71, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.56, default_y=-278.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.69, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.83, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.96, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.09, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.22, default_y=-258.71, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=302.12):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=58.76, default_y=-178.71, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.71, default_y=-163.71, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=187.63, default_y=-163.71, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=187.63, default_y=-153.71, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Staff(1)
            with Note(default_x=267.73, default_y=-143.71, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=230.59, default_y=-168.71, dynamics=40.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=230.59, default_y=-158.71, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-278.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.28, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.76, default_y=-233.71, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.24, default_y=-243.71, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.71, default_y=-233.71, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.19, default_y=-243.71, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.67, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.15, default_y=-223.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.63, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.11, default_y=-223.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.59, default_y=-258.71, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.06, default_y=-228.71, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=211.7):
            with Note(default_x=31.81, default_y=-108.71, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.44, default_y=-113.71, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.07, default_y=-118.71, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=126.71, default_y=-128.71, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=126.71, default_y=-118.71, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=165.46, default_y=-128.71, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=177.32, default_y=-123.71, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.81, default_y=-233.71, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=126.71, default_y=-223.71, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=177.32, default_y=-228.71, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='50', width=242.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.39)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=89.72, default_y=-141.39, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.5, default_y=-156.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=207.63, default_y=-156.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=154.5, default_y=-191.39, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=154.5, default_y=-176.39, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=89.72, default_y=-246.39, dynamics=55.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.5, default_y=-281.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='51', width=211.66):
            with Note(default_x=15.8, default_y=-156.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.18, default_y=-161.39, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.55, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.93, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.31, default_y=-171.39, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.69, default_y=-176.39, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-186.39, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-176.39, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=112.93, default_y=-181.39, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-276.39, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=112.93, default_y=-236.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=145.31, default_y=-241.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.69, default_y=-246.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='52', width=171.72):
            with Note(default_x=13.09, default_y=-176.39, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=92.16, default_y=-156.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=140.13, default_y=-156.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=13.09, default_y=-246.39, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=92.16, default_y=-256.39, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='53', width=392.88):
            with Note(default_x=14.0, default_y=-156.39, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=25.87, default_y=-151.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=55.76, default_y=-161.39, dynamics=40.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.76, default_y=-146.39, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=96.64, default_y=-166.39, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.64, default_y=-141.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.51, default_y=-166.39, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.51, default_y=-141.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=245.33, default_y=-146.39, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=267.18, default_y=-141.39, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('begin', number=4)
            with Note(default_x=282.85, default_y=-146.39, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('end', number=4)
            with Note(default_x=298.51, default_y=-141.39, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=320.36, default_y=-146.39, dynamics=40.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                    NormalType('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=350.41, default_y=-176.39, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=350.41, default_y=-141.39, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=245.33, default_y=-171.39, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=14.0, default_y=-256.39, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=96.64, default_y=-231.39, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=137.51, default_y=-236.39, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=245.33, default_y=-241.39, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=350.41, default_y=-246.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='54', width=123.72):
            with Note(default_x=14.21, default_y=-176.39, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=14.21, default_y=-141.39, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('3')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('3')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=14.21, default_y=-246.39, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('7')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')