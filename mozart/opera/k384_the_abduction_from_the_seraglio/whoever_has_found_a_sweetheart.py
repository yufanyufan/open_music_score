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
            PageHeight(1898.52)
            PageWidth(1343.09)
            with PageMargins(type='even'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Wer ein liebchen hat gefunden', default_x=671.547, default_y=1834.58, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Mozart', default_x=1279.15, default_y=1734.58, justify='right', valign='bottom', font_size='12')
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
        with Measure(number='1', width=202.02):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(84.98)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(-4)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.74, relative_y=20.0):
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
        with Measure(number='2', width=188.45):
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('1')
        with Measure(number='3', width=176.49):
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
            with Note(default_x=108.5, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wer')
            with Note(default_x=143.48, default_y=-25.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
        with Measure(number='4', width=193.4):
            with Note(default_x=25.72, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=75.14, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=111.48, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=160.9, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='5', width=171.23):
            with Note(default_x=17.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=43.11, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=68.41, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=119.02, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=144.33, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='6', width=198.65):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=15.8, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=47.81, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=79.83, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=112.78, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('red')
            with Note(default_x=164.0, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='7', width=277.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(138.63)
            with Note(default_x=112.58, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
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
            with Note(default_x=209.73, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('lohn')
            with Note(default_x=242.66, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='8', width=244.19):
            with Note(default_x=15.8, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ihr')
            with Note(default_x=56.27, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=96.74, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('durch')
            with Note(default_x=137.36, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tau')
            with Note(default_x=202.11, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('send')
        with Measure(number='9', width=222.2):
            with Note(default_x=22.56, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Küs')
            with Note(default_x=77.63, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=146.46, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mach')
            with Note(default_x=186.18, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='10', width=196.74):
            with Note(default_x=15.8, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('all')
            with Note(default_x=47.7, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=79.6, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('das')
            with Note(default_x=111.5, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=162.54, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='11', width=202.11):
            with Note(default_x=17.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=70.0, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.26, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sei')
            with Note(default_x=167.88, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='12', width=459.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(138.63)
            with Note(default_x=112.58, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tröst')
            with Note(default_x=170.05, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=227.52, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=285.0, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=399.94, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='13', width=348.17):
            with Note(default_x=36.69, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.92, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
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
            with Note(default_x=243.28, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=294.93, default_y=-25.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='14', width=335.22):
            with Note(default_x=15.8, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Trö')
            with Note(default_x=64.01, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=112.21, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=160.42, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=260.99, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='15', width=247.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(138.63)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=112.58, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.92, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=167.63, default_y=-35.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=212.77, default_y=-40.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='16', width=171.64):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note(default_x=36.77, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Freund')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=98.2, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tral')
            with Note(default_x=145.56, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='17', width=161.72):
            with Note(default_x=15.8, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=39.77, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
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
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=63.74, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=87.7, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=111.67, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
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
            with Note(default_x=135.64, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='18', width=140.64):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=47.28, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=74.78, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=106.26, default_y=10.0, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='19', width=262.24):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=15.8, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=48.45, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=81.1, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=113.75, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=146.41, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
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
            with Note(default_x=162.07, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=177.74, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
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
            with Note(default_x=193.4, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=210.7, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=227.99, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
        with Measure(number='20', width=159.03):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
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
            with Note(default_x=91.21, default_y=-25.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Doch')
            with Note(default_x=129.12, default_y=-25.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
        with Measure(number='21', width=315.16):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=108.9, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=177.12, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich')
            with Note(default_x=211.23, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=279.45, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='22', width=266.55):
            with Note(default_x=14.0, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('hal')
            with Note(default_x=54.58, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.16, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.94, default_y=-48.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.31, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.6, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text("schliess'")
            with Note(default_x=224.37, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=326.9):
            with Note(default_x=25.72, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=75.65, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chen')
            with Note(default_x=125.58, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=175.51, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sorg')
            with Note(default_x=275.37, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='24', width=233.8):
            with Note(default_x=18.34, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein;')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.18, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=196.74, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='25', width=363.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=108.9, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lo')
            with Note(default_x=148.22, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=187.54, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen')
            with Note(default_x=233.87, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ding')
            with Note(default_x=319.52, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
        with Measure(number='26', width=245.55):
            with Note(default_x=15.79, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=90.33, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('schen')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=164.87, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
            with Note(default_x=202.15, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='27', width=276.51):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=12.12, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmet')
            with Note(default_x=53.52, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.92, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=142.28, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling')
            with Note(default_x=231.05, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='28', width=256.4):
            with Note(default_x=14.0, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=97.96, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
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
            with Note(default_x=174.35, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=212.54, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='29', width=357.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=108.9, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=149.67, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=190.44, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=231.22, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Note(default_x=312.77, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='30', width=271.32):
            with Note(default_x=29.33, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=187.31, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=226.81, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='31', width=277.47):
            with Note(default_x=15.8, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=57.85, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
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
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=99.9, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=141.94, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=231.68, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='32', width=235.7):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=29.26, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.91, default_y=-45.99, relative_y=-30.0):
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
            with Note(default_x=102.81, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=142.76, default_y=-35.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=198.8, default_y=-40.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='33', width=278.58):
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
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=108.78, default_y=-45.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=180.89, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=240.02, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='34', width=222.16):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=15.8, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=49.93, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.05, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=118.18, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=152.3, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
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
            with Note(default_x=186.43, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='35', width=192.63):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=69.72, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=103.42, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=157.33, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='36', width=245.8):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=17.23, default_y=10.0, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=55.06, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=92.89, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=130.72, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=168.55, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
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
            with Note(default_x=206.38, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
        with Measure(number='37', width=203.24):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
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
            with Note(default_x=126.57, default_y=-25.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Son')
            with Note(default_x=164.1, default_y=-25.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
        with Measure(number='38', width=425.59):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=112.58, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=216.9, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('beim')
            with Note(default_x=268.67, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mon')
            with Note(default_x=372.22, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='39', width=335.61):
            with Note(default_x=14.0, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schei')
            with Note(default_x=67.33, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.67, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.91, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=227.34, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freun')
            with Note(default_x=280.67, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.02, default_y=-47.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='40', width=381.22):
            with Note(default_x=12.0, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('nehmt')
                    Extend()
            with Note(default_x=73.27, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=134.54, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=195.81, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl')
            with Note(default_x=318.35, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
        with Measure(number='41', width=350.87):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=108.78, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
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
            with Note(default_x=256.43, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=302.01, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('lauscht')
        with Measure(number='42', width=173.61):
            with Note(default_x=15.8, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                    Extend()
            with Note(default_x=42.24, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=68.67, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Note(default_x=99.14, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('jun')
            with Note(default_x=141.44, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges')
        with Measure(number='43', width=218.47):
            with Note(default_x=25.94, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Herr')
            with Note(default_x=79.01, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=145.34, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('kirrt')
            with Note(default_x=183.71, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='44', width=191.72):
            with Note(default_x=15.8, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('lockt')
                    Extend()
            with Note(default_x=49.34, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=79.36, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=112.08, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('klei')
            with Note(default_x=160.11, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='45', width=207.74):
            with Note(default_x=17.8, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Närr')
            with Note(default_x=67.36, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
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
            with Note(default_x=129.31, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=168.8, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='46', width=356.63):
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
            with Note(default_x=108.9, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-44.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Note(default_x=149.44, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=189.98, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=230.51, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=311.59, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='47', width=286.01):
            with Note(default_x=31.77, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-44.18, relative_y=-30.0):
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
            with Note(default_x=198.66, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=240.38, default_y=-25.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='48', width=295.43):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=15.8, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-44.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=57.54, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
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
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=99.28, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=141.02, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=224.5, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='49', width=204.35):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=31.81, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Note(default_x=121.92, default_y=-35.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=169.97, default_y=-40.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='50', width=266.05):
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
            with Note(default_x=109.72, default_y=-45.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=176.05, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=230.45, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='51', width=202.82):
            with Note(default_x=15.8, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=46.7, default_y=5.0, dynamics=93.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=77.61, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=108.51, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=139.41, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=170.31, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='52', width=166.13):
            with Note(default_x=13.09, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=58.93, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=90.03, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=135.87, default_y=10.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='53', width=375.29):
            with Note(default_x=14.0, default_y=10.0, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=53.25, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=92.51, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=131.76, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
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
                with Lyric(number='1', default_y=-45.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
                    Extend()
            with Note(default_x=150.68, default_y=5.0, dynamics=98.89):
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
            with Note(default_x=169.59, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=188.5, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('forward hook', number=4)
            with Note(default_x=204.17, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
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
            with Note(default_x=232.29, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=334.44, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('le')
        with Measure(number='54', width=132.13):
            with Note(default_x=14.21, default_y=-10.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.94, relative_y=-30.0):
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
        with Measure(number='1', width=202.02):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(82.92)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(-4)
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
            with Note(default_x=132.52, default_y=-137.92, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=167.65, default_y=-137.92):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=132.52, default_y=-172.92, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=132.52, default_y=-157.92, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=132.52, default_y=-262.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='2', width=188.45):
            with Note(default_x=12.0, default_y=-137.92, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.88, default_y=-142.92, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.75, default_y=-147.92, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=100.22, default_y=-172.92, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.22, default_y=-162.92, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=100.22, default_y=-147.92, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=129.09, default_y=-177.92, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.09, default_y=-152.92, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=157.97, default_y=-182.92, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=157.97, default_y=-157.92, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-167.92, dynamics=51.11):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-157.92, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=12.0, default_y=-257.92, dynamics=58.89):
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
            with Note(default_x=100.22, default_y=-252.92, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='3', width=176.49):
            with Note(default_x=15.8, default_y=-182.92, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=15.8, default_y=-172.92, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-157.92, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=77.08, default_y=-182.92, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=77.08, default_y=-172.92, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.08, default_y=-157.92, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-272.92, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=77.08, default_y=-272.92, dynamics=58.89):
                with Pitch():
                    Step('F')
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
        with Measure(number='4', width=193.4):
            with Note(default_x=25.72, default_y=-182.92, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=25.72, default_y=-172.92, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.72, default_y=-157.92, dynamics=62.22):
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
            with Note(default_x=111.48, default_y=-182.92, dynamics=45.56):
                with Pitch():
                    Step('A')
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
            with Note(default_x=111.48, default_y=-172.92, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=111.48, default_y=-157.92, dynamics=61.11):
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
            with Backup():
                Duration(720.0)
            with Note(default_x=25.72, default_y=-272.92, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=111.48, default_y=-262.92, dynamics=54.44):
                with Pitch():
                    Step('A')
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
        with Measure(number='5', width=171.23):
            with Note(default_x=17.8, default_y=-187.92, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=17.8, default_y=-172.92, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-162.92, dynamics=66.67):
                Chord()
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
            with Note(default_x=93.72, default_y=-172.92, dynamics=45.56):
                with Pitch():
                    Step('C')
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
            with Note(default_x=93.72, default_y=-157.92, dynamics=45.56):
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
            with Note(default_x=93.72, default_y=-147.92, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=17.8, default_y=-252.92, dynamics=60.0):
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
            with Note(default_x=93.72, default_y=-262.92, dynamics=54.44):
                with Pitch():
                    Step('A')
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
        with Measure(number='6', width=198.65):
            with Note(default_x=15.8, default_y=-147.92, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.81, default_y=-152.92, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.83, default_y=-157.92, dynamics=54.44):
                with Pitch():
                    Step('F')
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
            with Note(default_x=112.78, default_y=-157.92, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=164.0, default_y=-162.92, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-177.92, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-167.92, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=100.91, default_y=-177.92, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=112.78, default_y=-172.92, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-257.92, dynamics=58.89):
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
            with Note(default_x=112.78, default_y=-252.92, dynamics=54.44):
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
        with Measure(number='7', width=277.18):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.58, default_y=-165.0, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=112.58, default_y=-155.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=112.58, default_y=-140.0, dynamics=66.67):
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
            with Note(default_x=176.81, default_y=-155.0, dynamics=45.56):
                with Pitch():
                    Step('C')
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
            with Note(default_x=176.81, default_y=-140.0, dynamics=45.56):
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
            with Note(default_x=176.81, default_y=-130.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=112.58, default_y=-255.0, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=176.81, default_y=-220.0, dynamics=54.44):
                with Pitch():
                    Step('F')
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
        with Measure(number='8', width=244.19):
            with Note(default_x=15.8, default_y=-155.0, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-145.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-135.0, dynamics=66.67):
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
            with Note(default_x=137.36, default_y=-150.0, dynamics=57.78):
                with Pitch():
                    Step('D')
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
            with Note(default_x=137.36, default_y=-140.0, dynamics=57.78):
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
            with Note(default_x=149.23, default_y=-135.0, dynamics=52.22):
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
            with Note(default_x=15.8, default_y=-235.0, dynamics=60.0):
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
            with Note(default_x=137.36, default_y=-240.0, dynamics=54.44):
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
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=222.2):
            with Note(default_x=22.56, default_y=-155.0, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=22.56, default_y=-145.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=22.56, default_y=-135.0, dynamics=66.67):
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
            with Note(default_x=112.05, default_y=-155.0, dynamics=45.56):
                with Pitch():
                    Step('C')
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
            with Note(default_x=112.05, default_y=-140.0, dynamics=45.56):
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
            with Note(default_x=112.05, default_y=-130.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=22.56, default_y=-235.0, dynamics=60.0):
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
            with Note(default_x=112.05, default_y=-220.0, dynamics=54.44):
                with Pitch():
                    Step('F')
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
        with Measure(number='10', width=196.74):
            with Note(default_x=15.8, default_y=-155.0, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-145.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-135.0, dynamics=66.67):
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
            with Note(default_x=111.5, default_y=-150.0, dynamics=57.78):
                with Pitch():
                    Step('D')
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
            with Note(default_x=111.5, default_y=-140.0, dynamics=57.78):
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
            with Note(default_x=123.37, default_y=-135.0, dynamics=52.22):
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
            with Note(default_x=15.8, default_y=-235.0, dynamics=60.0):
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
            with Note(default_x=111.5, default_y=-240.0, dynamics=54.44):
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
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=202.11):
            with Note(default_x=17.8, default_y=-155.0, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=17.8, default_y=-145.0, dynamics=51.11):
                Chord()
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
            with Note(default_x=17.8, default_y=-135.0, dynamics=66.67):
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
            with Note(default_x=102.63, default_y=-180.0, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Octave(3)
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
            with Note(default_x=102.63, default_y=-170.0, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=102.63, default_y=-155.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.8, default_y=-235.0, dynamics=60.0):
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
            with Note(default_x=102.63, default_y=-270.0, dynamics=53.33):
                with Pitch():
                    Step('C')
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
        with Measure(number='12', width=459.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.58, default_y=-175.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.31, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.05, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=198.79, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.52, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=256.26, default_y=-165.0, dynamics=35.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.0, default_y=-170.0, dynamics=41.11):
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
            with Note(default_x=313.73, default_y=-160.0, dynamics=41.11):
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
            with Note(default_x=342.47, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=371.21, default_y=-160.0, dynamics=41.11):
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
            with Note(default_x=399.94, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=428.68, default_y=-160.0, dynamics=35.56):
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
            with Backup():
                Duration(720.0)
            with Note(default_x=112.58, default_y=-255.0, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=285.0, default_y=-270.0, dynamics=53.33):
                with Pitch():
                    Step('C')
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
        with Measure(number='13', width=348.17):
            with Note(default_x=36.69, default_y=-175.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.52, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.34, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=114.16, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.99, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=165.81, default_y=-165.0, dynamics=35.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=191.63, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.46, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=243.28, default_y=-140.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.1, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=294.93, default_y=-140.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.75, default_y=-155.0, dynamics=35.56):
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
            with Note(default_x=36.69, default_y=-255.0, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=191.63, default_y=-255.0, dynamics=54.44):
                with Pitch():
                    Step('F')
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
        with Measure(number='14', width=335.22):
            with Note(default_x=15.8, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.9, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=64.01, default_y=-140.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.11, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=112.21, default_y=-140.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.32, default_y=-155.0, dynamics=35.56):
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
            with Note(default_x=160.42, default_y=-160.0, dynamics=41.11):
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
            with Note(default_x=184.52, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=212.79, default_y=-145.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.89, default_y=-155.0, dynamics=41.11):
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
            with Note(default_x=260.99, default_y=-145.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.1, default_y=-155.0, dynamics=35.56):
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
            with Note(default_x=15.8, default_y=-220.0, dynamics=60.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=160.42, default_y=-235.0, dynamics=54.44):
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
        with Measure(number='15', width=247.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.9)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=112.58, default_y=-197.9, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=112.58, default_y=-172.9, dynamics=66.67):
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
            with Note(default_x=167.63, default_y=-152.9, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=167.63, default_y=-137.9, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=167.63, default_y=-127.9, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=212.77, default_y=-157.9, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=212.77, default_y=-142.9, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=212.77, default_y=-132.9, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=112.58, default_y=-287.9, dynamics=58.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=167.63, default_y=-232.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='16', width=171.64):
            with Note(default_x=36.77, default_y=-162.9, dynamics=40.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=36.77, default_y=-137.9, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=121.89, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.56, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=98.2, default_y=-187.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=36.77, default_y=-217.9, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=98.2, default_y=-252.9, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='17', width=161.72):
            with Note(default_x=15.8, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.77, default_y=-157.9, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.74, default_y=-162.9, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=87.7, default_y=-162.9, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.67, default_y=-167.9, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.64, default_y=-197.9, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=135.64, default_y=-172.9, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-182.9, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=87.7, default_y=-187.9, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-252.9, dynamics=61.11):
                with Pitch():
                    Step('F')
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
            with Note(default_x=87.7, default_y=-257.9, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=135.64, default_y=-252.9, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=140.64):
            with Note(default_x=15.8, default_y=-197.9, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-172.9, dynamics=60.0):
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
            with Note(default_x=74.78, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.26, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=74.78, default_y=-187.9, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=74.78, default_y=-172.9, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-252.9, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=74.78, default_y=-277.9, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='19', width=262.24):
            with Note(default_x=20.1, default_y=-152.9, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.45, default_y=-157.9, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.1, default_y=-162.9, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=113.75, default_y=-177.9, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.75, default_y=-162.9, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.41, default_y=-167.9, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.99, default_y=-172.9, dynamics=54.44):
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-172.9, dynamics=52.22):
                with Pitch():
                    Step('F')
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
            with Note(default_x=20.1, default_y=-182.9, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=113.75, default_y=-192.9, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-272.9, dynamics=65.56):
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
            with Note(default_x=113.75, default_y=-267.9, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='20', width=159.03):
            with Note(default_x=15.8, default_y=-197.9, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=15.8, default_y=-187.9, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-172.9, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=65.65, default_y=-197.9, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=65.65, default_y=-187.9, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=65.65, default_y=-172.9, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-252.9, dynamics=66.67):
                with Pitch():
                    Step('F')
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
            with Note(default_x=65.65, default_y=-252.9, dynamics=66.67):
                with Pitch():
                    Step('F')
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
        with Measure(number='21', width=315.16):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.49)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=143.01, default_y=-144.49, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.12, default_y=-129.49, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=245.34, default_y=-119.49, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=279.45, default_y=-129.49, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=108.9, default_y=-234.49, dynamics=66.67):
                with Pitch():
                    Step('A')
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
            with Note(default_x=211.23, default_y=-229.49, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=266.55):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=54.58, default_y=-134.49, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.16, default_y=-124.49, dynamics=48.89):
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
            with Note(default_x=176.31, default_y=-109.49, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=224.37, default_y=-119.49, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=14.0, default_y=-224.49, dynamics=66.67):
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
            with Note(default_x=135.74, default_y=-244.49, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='23', width=326.9):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=75.65, default_y=-124.49, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.58, default_y=-114.49, dynamics=48.89):
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
            with Note(default_x=225.44, default_y=-144.49, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.37, default_y=-134.49, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=25.72, default_y=-239.49, dynamics=66.67):
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
            with Note(default_x=175.51, default_y=-229.49, dynamics=61.11):
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
        with Measure(number='24', width=233.8):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.8, default_y=-129.49, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.26, default_y=-144.49, dynamics=48.89):
                with Pitch():
                    Step('C')
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
            with Note(default_x=160.18, default_y=-154.49, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=196.74, default_y=-164.49, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.34, default_y=-234.49, dynamics=66.67):
                with Pitch():
                    Step('A')
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
            with Note(default_x=124.72, default_y=-244.49, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='25', width=363.95):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.36)
                with StaffLayout(number=2):
                    StaffDistance(67.62)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=148.22, default_y=-124.36, dynamics=54.44):
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
            with Note(default_x=187.54, default_y=-119.36, dynamics=48.89):
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
            with Note(default_x=280.2, default_y=-114.36, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=319.52, default_y=-119.36, dynamics=48.89):
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
            with Note(default_x=108.9, default_y=-256.98, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.56, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.22, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=167.88, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.54, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=207.21, default_y=-246.98, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=233.87, default_y=-261.98, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.54, default_y=-251.98, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.2, default_y=-241.98, dynamics=41.11):
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
            with Note(default_x=299.86, default_y=-251.98, dynamics=41.11):
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
            with Note(default_x=319.52, default_y=-241.98, dynamics=41.11):
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
            with Note(default_x=339.18, default_y=-251.98, dynamics=35.56):
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
        with Measure(number='26', width=245.55):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.06, default_y=-109.36, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.33, default_y=-104.36, dynamics=48.89):
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
            with Note(default_x=164.87, default_y=-179.36, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.15, default_y=-174.36, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.79, default_y=-256.98, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.43, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.06, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=71.7, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.33, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=108.97, default_y=-246.98, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.6, default_y=-276.98, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.24, default_y=-241.98, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.87, default_y=-231.98, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.51, default_y=-241.98, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.15, default_y=-231.98, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.78, default_y=-241.98, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=276.51):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.52, default_y=-124.36, dynamics=54.44):
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
            with Note(default_x=94.92, default_y=-119.36, dynamics=48.89):
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
            with Note(default_x=189.65, default_y=-114.36, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.05, default_y=-119.36, dynamics=48.89):
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
            with Note(default_x=12.12, default_y=-256.98, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.82, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.52, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=74.22, default_y=-246.98, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.92, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=115.62, default_y=-246.98, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.28, default_y=-261.98, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.95, default_y=-251.98, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.65, default_y=-241.98, dynamics=41.11):
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
            with Note(default_x=210.35, default_y=-251.98, dynamics=41.11):
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
            with Note(default_x=231.05, default_y=-241.98, dynamics=41.11):
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
            with Note(default_x=251.75, default_y=-251.98, dynamics=35.56):
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
        with Measure(number='28', width=256.4):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=59.76, default_y=-109.36, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.96, default_y=-104.36, dynamics=48.89):
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
            with Note(default_x=174.35, default_y=-179.36, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=212.54, default_y=-174.36, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=14.0, default_y=-256.98, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.67, default_y=-246.98, dynamics=41.11):
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
            with Note(default_x=59.76, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=78.86, default_y=-246.98, dynamics=41.11):
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
            with Note(default_x=97.96, default_y=-236.98, dynamics=41.11):
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
            with Note(default_x=117.05, default_y=-246.98, dynamics=35.56):
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
            with Note(default_x=136.15, default_y=-256.98, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.25, default_y=-246.98, dynamics=41.11):
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
            with Note(default_x=174.35, default_y=-226.98, dynamics=41.11):
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
            with Note(default_x=193.44, default_y=-246.98, dynamics=41.11):
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
            with Note(default_x=212.54, default_y=-226.98, dynamics=41.11):
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
            with Note(default_x=231.64, default_y=-246.98, dynamics=35.56):
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
        with Measure(number='29', width=357.92):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.86)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.67, default_y=-141.86, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.44, default_y=-126.86, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=271.99, default_y=-126.86, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=312.77, default_y=-131.86, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=108.9, default_y=-276.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.28, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.67, default_y=-231.86, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.06, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.44, default_y=-231.86, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.83, default_y=-241.86, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=231.22, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=251.61, default_y=-236.86, dynamics=41.11):
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
            with Note(default_x=271.99, default_y=-226.86, dynamics=41.11):
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
            with Note(default_x=292.38, default_y=-236.86, dynamics=41.11):
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
            with Note(default_x=312.77, default_y=-226.86, dynamics=41.11):
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
            with Note(default_x=333.15, default_y=-236.86, dynamics=35.56):
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
        with Measure(number='30', width=271.32):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=68.82, default_y=-126.86, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=108.32, default_y=-116.86, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=187.31, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.81, default_y=-106.86, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=29.33, default_y=-266.86, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.07, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.82, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.57, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.32, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.07, default_y=-256.86, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.81, default_y=-276.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.56, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.31, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.06, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.81, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.55, default_y=-256.86, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=277.47):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=57.85, default_y=-141.86, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.9, default_y=-116.86, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=189.63, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.68, default_y=-121.86, dynamics=48.89):
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
            with Note(default_x=15.8, default_y=-276.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.82, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.85, default_y=-231.86, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.87, default_y=-241.86, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.9, default_y=-231.86, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.92, default_y=-241.86, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.94, default_y=-256.86, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.61, default_y=-246.86, dynamics=41.11):
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
            with Note(default_x=189.63, default_y=-226.86, dynamics=41.11):
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
            with Note(default_x=210.66, default_y=-246.86, dynamics=41.11):
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
            with Note(default_x=231.68, default_y=-226.86, dynamics=41.11):
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
            with Note(default_x=252.71, default_y=-246.86, dynamics=35.56):
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
        with Measure(number='32', width=235.7):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=57.28, default_y=-126.86, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.3, default_y=-151.86, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=170.78, default_y=-141.86, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.8, default_y=-166.86, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=29.26, default_y=-231.86, dynamics=66.67):
                with Pitch():
                    Step('A')
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
            with Note(default_x=142.76, default_y=-221.86, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=198.8, default_y=-226.86, dynamics=55.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=278.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.54)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.78, default_y=-166.54, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=180.89, default_y=-146.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=240.02, default_y=-146.54, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=180.89, default_y=-181.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=108.78, default_y=-236.54, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=180.89, default_y=-246.54, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='34', width=222.16):
            with Note(default_x=15.8, default_y=-146.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.93, default_y=-151.54, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=84.05, default_y=-156.54, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=118.18, default_y=-181.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.18, default_y=-156.54, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.3, default_y=-186.54, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.3, default_y=-161.54, dynamics=48.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=186.43, default_y=-191.54, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=186.43, default_y=-166.54, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-176.54, dynamics=60.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=15.8, default_y=-246.54, dynamics=61.11):
                with Pitch():
                    Step('F')
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
            with Note(default_x=118.18, default_y=-251.54, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=186.43, default_y=-246.54, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=192.63):
            with Note(default_x=15.8, default_y=-191.54, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-166.54, dynamics=60.0):
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
            with Note(default_x=103.42, default_y=-146.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=157.33, default_y=-146.54, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=91.55, default_y=-171.54, dynamics=45.56):
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
            with Note(default_x=103.42, default_y=-166.54, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-246.54, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=103.42, default_y=-271.54, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=245.8):
            with Note(default_x=17.23, default_y=-166.54, dynamics=45.56):
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
            with Note(default_x=17.23, default_y=-146.54, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.06, default_y=-151.54, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.89, default_y=-166.54, dynamics=45.56):
                with Pitch():
                    Step('F')
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
            with Note(default_x=92.89, default_y=-156.54, dynamics=56.67):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=130.72, default_y=-181.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.72, default_y=-166.54, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=130.72, default_y=-156.54, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=168.55, default_y=-186.54, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.55, default_y=-171.54, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=168.55, default_y=-161.54, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=206.38, default_y=-191.54, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=206.38, default_y=-166.54, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-176.54, dynamics=60.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=17.23, default_y=-266.54, dynamics=58.89):
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
            with Note(default_x=130.72, default_y=-261.54, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='37', width=203.24):
            with Note(default_x=15.8, default_y=-191.54, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=15.8, default_y=-181.54, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-166.54, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=89.03, default_y=-191.54, dynamics=51.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=89.03, default_y=-181.54, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=89.03, default_y=-166.54, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-246.54, dynamics=62.22):
                with Pitch():
                    Step('F')
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
            with Note(default_x=89.03, default_y=-246.54, dynamics=62.22):
                with Pitch():
                    Step('F')
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
        with Measure(number='38', width=425.59):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.51)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.58, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.24, default_y=-138.51, dynamics=54.44):
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
            with Note(default_x=165.13, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.02, default_y=-128.51, dynamics=54.44):
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
            with Note(default_x=216.9, default_y=-123.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.79, default_y=-128.51, dynamics=48.89):
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
            with Note(default_x=268.67, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.56, default_y=-138.51, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.45, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.33, default_y=-128.51, dynamics=54.44):
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
            with Note(default_x=372.22, default_y=-123.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.1, default_y=-133.51, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=112.58, default_y=-228.51, dynamics=66.67):
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
            with Note(default_x=268.67, default_y=-238.51, dynamics=61.11):
                with Pitch():
                    Step('A')
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
        with Measure(number='39', width=335.61):
            with Note(default_x=14.0, default_y=-138.51, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.67, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.33, default_y=-128.51, dynamics=54.44):
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
            with Note(default_x=94.0, default_y=-148.51, dynamics=54.44):
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
            with Note(default_x=120.67, default_y=-143.51, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.34, default_y=-138.51, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.0, default_y=-133.51, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.67, default_y=-128.51, dynamics=54.44):
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
            with Note(default_x=227.34, default_y=-123.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.01, default_y=-118.51, dynamics=54.44):
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
            with Note(default_x=280.67, default_y=-113.51, dynamics=54.44):
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
            with Note(default_x=307.34, default_y=-123.51, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=14.0, default_y=-243.51, dynamics=66.67):
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
            with Note(default_x=174.0, default_y=-248.51, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='40', width=381.22):
            with Note(default_x=12.0, default_y=-128.51, dynamics=54.44):
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
            with Note(default_x=42.63, default_y=-123.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.27, default_y=-118.51, dynamics=54.44):
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
            with Note(default_x=103.9, default_y=-113.51, dynamics=54.44):
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
            with Note(default_x=134.54, default_y=-108.51, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.17, default_y=-118.51, dynamics=48.89):
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
            with Note(default_x=195.81, default_y=-123.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.44, default_y=-118.51, dynamics=54.44):
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
            with Note(default_x=257.08, default_y=-113.51, dynamics=54.44):
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
            with Note(default_x=287.71, default_y=-148.51, dynamics=54.44):
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
            with Note(default_x=318.35, default_y=-143.51, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.98, default_y=-138.51, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-243.51, dynamics=66.67):
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
            with Note(default_x=195.81, default_y=-238.51, dynamics=61.11):
                with Pitch():
                    Step('A')
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
            with Note(default_x=318.35, default_y=-233.51, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=350.87):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.4)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=108.78, default_y=-107.4, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.21, default_y=-117.4, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.63, default_y=-122.4, dynamics=54.44):
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
            with Note(default_x=167.06, default_y=-127.4, dynamics=54.44):
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
            with Note(default_x=186.49, default_y=-132.4, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.92, default_y=-137.4, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.35, default_y=-142.4, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=108.78, default_y=-212.4, dynamics=66.67):
                with Pitch():
                    Step('A')
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
            with Note(default_x=225.35, default_y=-202.4, dynamics=61.11):
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
        with Measure(number='42', width=173.61):
            with Note(default_x=15.8, default_y=-157.4, dynamics=63.33):
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-147.4, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-137.4, dynamics=57.78):
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
            with Note(default_x=99.14, default_y=-152.4, dynamics=57.78):
                with Pitch():
                    Step('D')
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
            with Note(default_x=99.14, default_y=-142.4, dynamics=57.78):
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
            with Note(default_x=111.01, default_y=-137.4, dynamics=52.22):
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
            with Note(default_x=15.8, default_y=-237.4, dynamics=60.0):
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
            with Note(default_x=99.14, default_y=-242.4, dynamics=54.44):
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
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=218.47):
            with Note(default_x=25.94, default_y=-157.4, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=25.94, default_y=-147.4, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.94, default_y=-137.4, dynamics=66.67):
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
            with Note(default_x=112.18, default_y=-157.4, dynamics=45.56):
                with Pitch():
                    Step('C')
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
            with Note(default_x=112.18, default_y=-142.4, dynamics=45.56):
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
            with Note(default_x=112.18, default_y=-132.4, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=25.94, default_y=-237.4, dynamics=60.0):
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
            with Note(default_x=112.18, default_y=-222.4, dynamics=54.44):
                with Pitch():
                    Step('F')
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
        with Measure(number='44', width=191.72):
            with Note(default_x=15.8, default_y=-157.4, dynamics=51.11):
                with Pitch():
                    Step('C')
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
            with Note(default_x=15.8, default_y=-147.4, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-137.4, dynamics=66.67):
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
            with Note(default_x=112.08, default_y=-152.4, dynamics=57.78):
                with Pitch():
                    Step('D')
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
            with Note(default_x=112.08, default_y=-142.4, dynamics=57.78):
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
            with Note(default_x=123.95, default_y=-137.4, dynamics=52.22):
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
            with Note(default_x=15.8, default_y=-237.4, dynamics=60.0):
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
            with Note(default_x=112.08, default_y=-242.4, dynamics=54.44):
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
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=207.74):
            with Note(default_x=17.8, default_y=-157.4, dynamics=63.33):
                with Pitch():
                    Step('C')
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
            with Note(default_x=17.8, default_y=-147.4, dynamics=63.33):
                Chord()
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
            with Note(default_x=17.8, default_y=-137.4, dynamics=57.78):
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
            with Note():
                Rest()
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.8, default_y=-237.4, dynamics=60.0):
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
            with Note():
                Rest()
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='46', width=356.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.44, default_y=-175.05, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.98, default_y=-160.05, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=271.05, default_y=-160.05, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=311.59, default_y=-165.05, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=108.9, default_y=-275.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.17, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.44, default_y=-230.05, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.71, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.98, default_y=-230.05, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.25, default_y=-240.05, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=230.51, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.78, default_y=-235.05, dynamics=41.11):
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
            with Note(default_x=271.05, default_y=-225.05, dynamics=41.11):
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
            with Note(default_x=291.32, default_y=-235.05, dynamics=41.11):
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
            with Note(default_x=311.59, default_y=-225.05, dynamics=41.11):
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
            with Note(default_x=331.86, default_y=-235.05, dynamics=35.56):
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
        with Measure(number='47', width=286.01):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=73.49, default_y=-160.05, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=115.21, default_y=-150.05, dynamics=48.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=198.66, default_y=-150.05, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.38, default_y=-140.05, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.77, default_y=-265.05, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.63, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.49, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.35, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.21, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.08, default_y=-255.05, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.94, default_y=-275.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.8, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.66, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.52, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.38, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.24, default_y=-255.05, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=295.43):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=57.54, default_y=-175.05, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.28, default_y=-160.05, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=182.76, default_y=-160.05, dynamics=45.56):
                with Pitch():
                    Step('F')
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
            with Note(default_x=182.76, default_y=-150.05, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note(default_x=261.04, default_y=-140.05, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=224.5, default_y=-165.05, dynamics=40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=224.5, default_y=-155.05, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-275.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.67, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.54, default_y=-230.05, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.41, default_y=-240.05, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.28, default_y=-230.05, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.15, default_y=-240.05, dynamics=35.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.02, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.89, default_y=-220.05, dynamics=41.11):
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
            with Note(default_x=182.76, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.63, default_y=-220.05, dynamics=41.11):
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
            with Note(default_x=224.5, default_y=-255.05, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.37, default_y=-225.05, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=204.35):
            with Note(default_x=31.81, default_y=-105.05, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.84, default_y=-110.05, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=91.88, default_y=-115.05, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=121.92, default_y=-125.05, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=121.92, default_y=-115.05, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=158.11, default_y=-125.05, dynamics=45.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.97, default_y=-120.05, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.81, default_y=-230.05, dynamics=66.67):
                with Pitch():
                    Step('A')
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
            with Note(default_x=121.92, default_y=-220.05, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.97, default_y=-225.05, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='50', width=266.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.39)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=109.72, default_y=-151.39, dynamics=48.89):
                with Pitch():
                    Step('F')
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
            with Note(default_x=176.05, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=230.45, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=176.05, default_y=-201.39, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=176.05, default_y=-186.39, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=109.72, default_y=-256.39, dynamics=55.56):
                with Pitch():
                    Step('A')
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
            with Note(default_x=176.05, default_y=-291.39, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='51', width=202.82):
            with Note(default_x=15.8, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.7, default_y=-171.39, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=77.61, default_y=-176.39, dynamics=54.44):
                with Pitch():
                    Step('A')
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
            with Note(default_x=108.51, default_y=-176.39, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=139.41, default_y=-181.39, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.31, default_y=-186.39, dynamics=54.44):
                with Pitch():
                    Step('F')
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
            with Note(default_x=15.8, default_y=-196.39, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-186.39, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=108.51, default_y=-191.39, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-286.39, dynamics=58.89):
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
            with Note(default_x=108.51, default_y=-246.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.41, default_y=-251.39, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.31, default_y=-256.39, dynamics=54.44):
                with Pitch():
                    Step('A')
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
        with Measure(number='52', width=166.13):
            with Note(default_x=13.09, default_y=-186.39, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=90.03, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=135.87, default_y=-166.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=13.09, default_y=-256.39, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=90.03, default_y=-266.39, dynamics=61.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='53', width=375.29):
            with Note(default_x=14.0, default_y=-166.39, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=25.87, default_y=-161.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=53.25, default_y=-171.39, dynamics=40.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.25, default_y=-156.39, dynamics=55.56):
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
            with Note(default_x=92.51, default_y=-176.39, dynamics=45.56):
                with Pitch():
                    Step('A')
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
            with Note(default_x=92.51, default_y=-151.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.76, default_y=-176.39, dynamics=45.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.76, default_y=-151.39, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=232.29, default_y=-156.39, dynamics=45.56):
                with Pitch():
                    Step('E')
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
            with Note(default_x=253.27, default_y=-151.39, dynamics=61.11):
                with Pitch():
                    Step('F')
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
            with Note(default_x=268.94, default_y=-156.39, dynamics=45.56):
                with Pitch():
                    Step('E')
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
            with Note(default_x=284.6, default_y=-151.39, dynamics=61.11):
                with Pitch():
                    Step('F')
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
            with Note(default_x=305.59, default_y=-156.39, dynamics=40.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=334.44, default_y=-186.39, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=334.44, default_y=-151.39, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=232.29, default_y=-181.39, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=14.0, default_y=-266.39, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=92.51, default_y=-241.39, dynamics=54.44):
                with Pitch():
                    Step('D')
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
            with Note(default_x=131.76, default_y=-246.39, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=232.29, default_y=-251.39, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=334.44, default_y=-256.39, dynamics=54.44):
                with Pitch():
                    Step('A')
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
        with Measure(number='54', width=132.13):
            with Note(default_x=14.21, default_y=-186.39, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=14.21, default_y=-151.39, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=14.21, default_y=-256.39, dynamics=66.67):
                with Pitch():
                    Step('A')
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