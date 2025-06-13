with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Title')
    with Identification():
        Creator('Composer', type='composer')
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
        with Measure(number='1', width=173.74):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(84.98)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(1)
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
        with Measure(number='2', width=202.29):
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('1')
        with Measure(number='3', width=178.25):
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
            with Note(default_x=109.81, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wer')
            with Note(default_x=144.79, default_y=-30.0, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
        with Measure(number='4', width=195.16):
            with Note(default_x=25.72, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=75.81, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=112.15, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=162.25, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='5', width=177.87):
            with Note(default_x=16.2, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-58.13, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=42.88, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=69.56, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.91, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=149.59, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='6', width=202.94):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-58.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=48.93, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=82.06, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=115.19, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('red')
            with Note(default_x=168.2, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='7', width=252.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(143.58)
            with Note(default_x=83.41, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
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
            with Note(default_x=183.39, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('lohn')
            with Note(default_x=217.27, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='8', width=248.92):
            with Note(default_x=15.8, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ihr')
            with Note(default_x=57.14, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=98.48, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('durch')
            with Note(default_x=139.83, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tau')
            with Note(default_x=205.97, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('send')
        with Measure(number='9', width=226.93):
            with Note(default_x=22.56, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Küs')
            with Note(default_x=79.27, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.17, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mach')
            with Note(default_x=189.88, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='10', width=201.47):
            with Note(default_x=15.8, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('all')
            with Note(default_x=48.67, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.54, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('das')
            with Note(default_x=114.41, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=167.0, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='11', width=212.35):
            with Note(default_x=16.2, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=71.79, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=141.27, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sei')
            with Note(default_x=176.01, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='12', width=439.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(143.58)
            with Note(default_x=83.41, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tröst')
            with Note(default_x=142.47, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=201.52, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=260.58, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=378.69, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='13', width=357.66):
            with Note(default_x=36.69, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=249.61, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=302.84, default_y=-30.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='14', width=345.41):
            with Note(default_x=15.8, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Trö')
            with Note(default_x=65.92, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.05, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster,')
            with Note(default_x=166.17, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=270.22, default_y=-10.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='15', width=234.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(143.58)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=83.41, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=147.63, default_y=-40.0, dynamics=94.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=200.3, default_y=-45.0, dynamics=94.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
        with Measure(number='16', width=174.14):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note(default_x=36.77, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('E')
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
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=99.45, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tral')
            with Note(default_x=148.06, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='17', width=164.22):
            with Note(default_x=15.8, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
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
            with Note(default_x=40.27, default_y=0.0, dynamics=88.89):
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
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=64.74, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=89.21, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=113.67, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=138.14, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='18', width=143.14):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=48.54, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
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
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=76.03, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=108.76, default_y=5.0, dynamics=94.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='19', width=264.56):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=13.09, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=46.57, default_y=0.0, dynamics=94.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=80.05, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=113.53, default_y=-5.0, dynamics=94.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.46, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=147.01, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=162.68, default_y=-5.0, dynamics=88.89):
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
            with Note(default_x=178.35, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=194.01, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=211.74, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=229.48, default_y=-15.0, dynamics=94.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
        with Measure(number='20', width=161.54):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=93.71, default_y=-30.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Doch')
            with Note(default_x=131.62, default_y=-30.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
        with Measure(number='21', width=222.34):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Attributes():
                with Key():
                    Fifths(1)
            with Note(default_x=79.73, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=122.76, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich')
            with Note(default_x=152.56, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=195.59, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='22', width=209.85):
            with Note(default_x=17.23, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-56.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('hal')
            with Note(default_x=45.82, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=74.42, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.94, default_y=-56.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=131.6, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.6, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text("schliess'")
            with Note(default_x=179.66, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=266.97):
            with Note(default_x=25.72, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lieb')
            with Note(default_x=69.04, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=4.08, default_y=-56.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chen')
            with Note(default_x=112.6, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=153.89, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sorg')
            with Note(default_x=228.21, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='24', width=170.15):
            with Note(default_x=18.34, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein;')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=102.32, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=138.88, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='25', width=273.11):
            with Note(default_x=12.12, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-56.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lo')
            with Note(default_x=51.32, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=90.53, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen')
            with Note(default_x=140.03, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ding')
            with Note(default_x=228.74, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
        with Measure(number='26', width=317.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=79.73, default_y=-20.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=157.28, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('schen')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=234.82, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
            with Note(default_x=273.6, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='27', width=292.21):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=12.12, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schmet')
            with Note(default_x=55.57, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.02, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=150.64, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling')
            with Note(default_x=245.72, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='28', width=271.61):
            with Note(default_x=17.23, default_y=-20.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=107.04, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
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
            with Note(default_x=186.93, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=226.88, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='29', width=260.84):
            with Note(default_x=15.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=55.85, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.9, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=135.95, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Note(default_x=216.05, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='30', width=312.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=79.73, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=230.79, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=268.56, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='31', width=271.67):
            with Note(default_x=15.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('gern')
                    Extend()
            with Note(default_x=56.04, default_y=0.0, dynamics=93.33):
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
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=96.28, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=136.52, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=226.78, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='32', width=229.9):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=29.26, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.91, default_y=-50.94, relative_y=-30.0):
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
            with Note(default_x=97.26, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.2, default_y=-40.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frem')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Sound(tempo=63.0)
            with Note(default_x=193.0, default_y=-45.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
        with Measure(number='33', width=152.8):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=29.33, default_y=-50.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=78.28, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=118.43, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='34', width=175.83):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=15.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=42.2, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=68.61, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=95.01, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=121.42, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=147.82, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='35', width=214.09):
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
            with Note(default_x=83.41, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=116.46, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-53.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=146.66, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=179.71, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='36', width=203.37):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=17.23, default_y=5.0, dynamics=104.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=47.08, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-53.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=76.93, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=106.77, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=142.08, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=171.93, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
        with Measure(number='37', width=157.08):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Sound(tempo=62.0)
            with Note(default_x=15.8, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
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
            with Note(default_x=91.96, default_y=-30.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Son')
            with Note(default_x=124.91, default_y=-30.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=4.08, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
        with Measure(number='38', width=284.15):
            with Note(default_x=21.88, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=113.56, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('beim')
            with Note(default_x=156.42, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mon')
            with Note(default_x=238.79, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='39', width=283.72):
            with Note(default_x=17.23, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-53.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schei')
            with Note(default_x=59.13, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=109.98, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.91, default_y=-53.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=193.79, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freun')
            with Note(default_x=238.01, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.02, default_y=-53.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
        with Measure(number='40', width=422.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=79.61, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('nehmt')
                    Extend()
            with Note(default_x=135.98, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.35, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=248.71, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl')
            with Note(default_x=363.16, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
        with Measure(number='41', width=286.2):
            with Note(default_x=23.46, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
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
            with Note(default_x=191.76, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=237.34, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('lauscht')
        with Measure(number='42', width=194.25):
            with Note(default_x=15.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                    Extend()
            with Note(default_x=47.38, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=78.96, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Note(default_x=110.54, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('jun')
            with Note(default_x=161.07, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges')
        with Measure(number='43', width=239.12):
            with Note(default_x=25.94, default_y=-20.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Herr')
            with Note(default_x=86.19, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen,')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=161.5, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('kirrt')
            with Note(default_x=199.86, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='44', width=296.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=83.41, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('lockt')
                    Extend()
            with Note(default_x=121.24, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=159.06, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=196.89, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('klei')
            with Note(default_x=257.4, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='45', width=248.46):
            with Note(default_x=21.03, default_y=-20.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Närr')
            with Note(default_x=85.55, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
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
            with Note(default_x=166.21, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=206.53, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='46', width=287.32):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Note(default_x=60.66, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.53, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=150.39, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=240.12, default_y=-20.0, dynamics=98.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='47', width=309.8):
            with Note(default_x=31.77, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-49.18, relative_y=-30.0):
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
            with Note(default_x=215.96, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=262.01, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
        with Measure(number='48', width=380.33):
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
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=83.41, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Treu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=128.3, default_y=0.0, dynamics=93.33):
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
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=173.18, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=218.06, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=307.83, default_y=-10.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='49', width=204.81):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=31.81, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Note(default_x=122.22, default_y=-40.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=170.43, default_y=-45.0, dynamics=98.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='50', width=186.97):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Sound(tempo=61.0)
            with Note(default_x=31.81, default_y=-50.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=97.64, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=151.63, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='51', width=205.36):
            with Note(default_x=15.8, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=47.13, default_y=0.0, dynamics=93.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=78.45, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=109.78, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tra')
            with Note(default_x=141.11, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.43, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='52', width=164.95):
            with Note(default_x=13.09, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=58.48, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=89.58, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tra')
            with Note(default_x=134.98, default_y=5.0, dynamics=98.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('la')
        with Measure(number='53', width=733.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.8)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=91.65, default_y=5.0, dynamics=104.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=162.53, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra,')
            with Note(default_x=233.41, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tral')
            with Note(default_x=304.29, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
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
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
                    Extend()
            with Note(default_x=338.44, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=372.59, default_y=-5.0, dynamics=98.89):
                with Pitch():
                    Step('G')
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
            with Note(default_x=406.74, default_y=0.0, dynamics=98.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('forward hook', number=4)
            with Note(default_x=434.99, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(45.0)
                Voice('1')
                Type('32nd')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=485.77, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=661.0, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('le')
        with Measure(number='54', width=408.94):
            with Note(default_x=14.21, default_y=-15.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
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
        with Measure(number='1', width=173.74):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(80.57)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(1)
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
            with Note(default_x=103.35, default_y=-140.57, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=139.36, default_y=-140.57):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=103.35, default_y=-175.57, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=103.35, default_y=-160.57, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=103.35, default_y=-265.57):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='2', width=202.29):
            with Note(default_x=15.8, default_y=-140.57, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.36, default_y=-145.57, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.93, default_y=-150.57, dynamics=54.44):
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
            with Note(default_x=107.49, default_y=-175.57, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.49, default_y=-160.57, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=107.49, default_y=-150.57, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=138.06, default_y=-180.57, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.06, default_y=-155.57, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=170.12, default_y=-185.57, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=170.12, default_y=-160.57, dynamics=54.44):
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
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-170.57, dynamics=51.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-160.57, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note(default_x=15.8, default_y=-260.57, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=107.49, default_y=-255.57, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='3', width=178.25):
            with Note(default_x=15.8, default_y=-185.57, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=15.8, default_y=-175.57, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-160.57, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=77.95, default_y=-185.57, dynamics=51.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.95, default_y=-175.57, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.95, default_y=-160.57, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=15.8, default_y=-275.57, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=77.95, default_y=-275.57, dynamics=58.89):
                with Pitch():
                    Step('E')
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
        with Measure(number='4', width=195.16):
            with Note(default_x=25.72, default_y=-185.57, dynamics=51.11):
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
            with Note(default_x=25.72, default_y=-175.57, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.72, default_y=-160.57, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=112.15, default_y=-185.57, dynamics=45.56):
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
            with Note(default_x=112.15, default_y=-175.57, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=112.15, default_y=-160.57, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=25.72, default_y=-275.57, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=112.15, default_y=-265.57, dynamics=54.44):
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
        with Measure(number='5', width=177.87):
            with Note(default_x=16.2, default_y=-190.57, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=16.2, default_y=-175.57, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-160.57, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=96.24, default_y=-175.57, dynamics=45.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=96.24, default_y=-160.57, dynamics=45.56):
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
            with Note(default_x=96.24, default_y=-150.57, dynamics=61.11):
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
            with Note(default_x=16.2, default_y=-255.57, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=96.24, default_y=-265.57, dynamics=54.44):
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
        with Measure(number='6', width=202.94):
            with Note(default_x=15.8, default_y=-150.57, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=48.93, default_y=-155.57, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=82.06, default_y=-160.57, dynamics=54.44):
                with Pitch():
                    Step('E')
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
            with Note(default_x=115.19, default_y=-160.57, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.2, default_y=-160.57, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-180.57, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-170.57, dynamics=66.67):
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
            with Note(default_x=103.33, default_y=-180.57, dynamics=45.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=115.19, default_y=-175.57, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-260.57, dynamics=58.89):
                with Pitch():
                    Step('A')
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
            with Note(default_x=115.19, default_y=-255.57, dynamics=54.44):
                with Pitch():
                    Step('B')
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
        with Measure(number='7', width=252.74):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-170.0, dynamics=51.11):
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
            with Note(default_x=83.41, default_y=-160.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=83.41, default_y=-145.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=149.51, default_y=-160.0, dynamics=45.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=149.51, default_y=-145.0, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=149.51, default_y=-135.0, dynamics=61.11):
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
            with Note(default_x=83.41, default_y=-260.0, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=149.51, default_y=-225.0, dynamics=54.44):
                with Pitch():
                    Step('E')
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
        with Measure(number='8', width=248.92):
            with Note(default_x=15.8, default_y=-160.0, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-150.0, dynamics=51.11):
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
            with Note(default_x=15.8, default_y=-140.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=139.83, default_y=-150.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=151.69, default_y=-145.0, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=139.83, default_y=-140.0, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-240.0, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=139.83, default_y=-240.0, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=226.93):
            with Note(default_x=22.56, default_y=-160.0, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=22.56, default_y=-150.0, dynamics=51.11):
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
            with Note(default_x=22.56, default_y=-140.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.72, default_y=-160.0, dynamics=45.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=114.72, default_y=-145.0, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.72, default_y=-135.0, dynamics=61.11):
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
            with Note(default_x=22.56, default_y=-240.0, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=114.72, default_y=-225.0, dynamics=54.44):
                with Pitch():
                    Step('E')
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
        with Measure(number='10', width=201.47):
            with Note(default_x=15.8, default_y=-160.0, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-150.0, dynamics=51.11):
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
            with Note(default_x=15.8, default_y=-140.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.41, default_y=-150.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=126.27, default_y=-145.0, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.41, default_y=-140.0, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-240.0, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=114.41, default_y=-240.0, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=212.35):
            with Note(default_x=16.2, default_y=-160.0, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=16.2, default_y=-145.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=28.07, default_y=-140.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=106.53, default_y=-180.0, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.39, default_y=-175.0, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=106.53, default_y=-160.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=16.2, default_y=-240.0, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=106.53, default_y=-275.0, dynamics=53.33):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=439.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-180.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.94, default_y=-170.0, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.47, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.0, default_y=-170.0, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.52, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.05, default_y=-170.0, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.58, default_y=-175.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=290.11, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.63, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.16, default_y=-165.0, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.69, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.22, default_y=-165.0, dynamics=35.56):
                with Pitch():
                    Step('A')
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
            with Note(default_x=83.41, default_y=-260.0, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=260.58, default_y=-275.0, dynamics=53.33):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=357.66):
            with Note(default_x=36.69, default_y=-180.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=63.31, default_y=-170.0, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.92, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.54, default_y=-170.0, dynamics=41.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.15, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.76, default_y=-170.0, dynamics=35.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.38, default_y=-170.0, dynamics=41.11):
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
            with Note(default_x=222.99, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.61, default_y=-145.0, dynamics=41.11):
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
            with Note(default_x=276.22, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.84, default_y=-145.0, dynamics=41.11):
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
            with Note(default_x=329.45, default_y=-160.0, dynamics=35.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=36.69, default_y=-260.0, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=196.38, default_y=-260.0, dynamics=54.44):
                with Pitch():
                    Step('E')
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
        with Measure(number='14', width=345.41):
            with Note(default_x=15.8, default_y=-170.0, dynamics=41.11):
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
            with Note(default_x=40.86, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.92, default_y=-145.0, dynamics=41.11):
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
            with Note(default_x=90.98, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.05, default_y=-145.0, dynamics=41.11):
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
            with Note(default_x=141.11, default_y=-160.0, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.17, default_y=-165.0, dynamics=41.11):
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
            with Note(default_x=191.23, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.1, default_y=-145.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.16, default_y=-160.0, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.22, default_y=-145.0, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.28, default_y=-160.0, dynamics=35.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-225.0, dynamics=60.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=166.17, default_y=-240.0, dynamics=54.44):
                with Pitch():
                    Step('B')
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
        with Measure(number='15', width=234.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.4)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=83.41, default_y=-190.4, dynamics=51.11):
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
            with Note(default_x=83.41, default_y=-165.4, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=147.63, default_y=-145.4, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=147.63, default_y=-130.4, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=147.63, default_y=-120.4, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=200.3, default_y=-150.4, dynamics=45.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.44, default_y=-130.4, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=200.3, default_y=-125.4, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=83.41, default_y=-280.4, dynamics=58.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=147.63, default_y=-225.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='16', width=174.14):
            with Note(default_x=36.77, default_y=-155.4, dynamics=40.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=36.77, default_y=-130.4, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=123.76, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.06, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=99.45, default_y=-180.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=36.77, default_y=-210.4, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=99.45, default_y=-245.4, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='17', width=164.22):
            with Note(default_x=15.8, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.27, default_y=-150.4, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.74, default_y=-155.4, dynamics=54.44):
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
            with Note(default_x=89.21, default_y=-155.4, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.67, default_y=-160.4, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.14, default_y=-190.4, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=138.14, default_y=-165.4, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-175.4, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=89.21, default_y=-180.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
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
            with Note(default_x=15.8, default_y=-245.4, dynamics=61.11):
                with Pitch():
                    Step('E')
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
            with Note(default_x=89.21, default_y=-245.4, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=138.14, default_y=-245.4, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=143.14):
            with Note(default_x=15.8, default_y=-190.4, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-165.4, dynamics=60.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=76.03, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=108.76, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=76.03, default_y=-180.4, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=76.03, default_y=-165.4, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=15.8, default_y=-245.4, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=76.03, default_y=-270.4, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='19', width=264.56):
            with Note(default_x=17.39, default_y=-145.4, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.57, default_y=-150.4, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.05, default_y=-155.4, dynamics=54.44):
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
            with Note(default_x=113.53, default_y=-165.4, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.53, default_y=-155.4, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=147.01, default_y=-160.4, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=229.48, default_y=-165.4, dynamics=54.44):
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
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(default_x=13.09, default_y=-165.4, dynamics=52.22):
                with Pitch():
                    Step('E')
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
            with Note(default_x=17.39, default_y=-175.4, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=113.53, default_y=-185.4, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=13.09, default_y=-265.4, dynamics=65.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=113.53, default_y=-260.4, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='20', width=161.54):
            with Note(default_x=15.8, default_y=-190.4, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=15.8, default_y=-180.4, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-165.4, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=67.31, default_y=-190.4, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=67.31, default_y=-180.4, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
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
            with Note(default_x=67.31, default_y=-165.4, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=15.8, default_y=-245.4, dynamics=66.67):
                with Pitch():
                    Step('E')
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
            with Note(default_x=67.31, default_y=-245.4, dynamics=66.67):
                with Pitch():
                    Step('E')
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
        with Measure(number='21', width=222.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.17)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=101.25, default_y=-152.17, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=122.76, default_y=-137.17, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=174.07, default_y=-127.17, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.59, default_y=-137.17, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=79.73, default_y=-242.17, dynamics=66.67):
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
            with Note(default_x=152.56, default_y=-237.17, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
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
        with Measure(number='22', width=209.85):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=45.82, default_y=-142.17, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.42, default_y=-132.17, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=131.6, default_y=-117.17, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.66, default_y=-127.17, dynamics=48.89):
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
            with Note(default_x=17.23, default_y=-232.17, dynamics=66.67):
                with Pitch():
                    Step('B')
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
            with Note(default_x=103.01, default_y=-252.17, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='23', width=266.97):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.04, default_y=-132.17, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=112.6, default_y=-122.17, dynamics=48.89):
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
            with Note(default_x=191.05, default_y=-152.17, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=228.21, default_y=-142.17, dynamics=48.89):
                with Pitch():
                    Step('D')
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
            with Note(default_x=25.72, default_y=-247.17, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=153.89, default_y=-237.17, dynamics=61.11):
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
        with Measure(number='24', width=170.15):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=39.34, default_y=-137.17, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=60.33, default_y=-152.17, dynamics=48.89):
                with Pitch():
                    Step('B')
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
            with Note(default_x=102.32, default_y=-162.17, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.88, default_y=-172.17, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.34, default_y=-242.17, dynamics=66.67):
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
            with Note(default_x=81.33, default_y=-252.17, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='25', width=273.11):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=51.32, default_y=-137.17, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.53, default_y=-132.17, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=189.53, default_y=-127.17, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=228.74, default_y=-132.17, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-267.17, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.72, default_y=-257.17, dynamics=41.11):
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
            with Note(default_x=51.32, default_y=-247.17, dynamics=41.11):
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
            with Note(default_x=70.93, default_y=-257.17, dynamics=41.11):
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
            with Note(default_x=90.53, default_y=-247.17, dynamics=41.11):
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
            with Note(default_x=110.13, default_y=-257.17, dynamics=35.56):
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
            with Note(default_x=140.03, default_y=-272.17, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.93, default_y=-262.17, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.53, default_y=-252.17, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.13, default_y=-262.17, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.74, default_y=-252.17, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.34, default_y=-262.17, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=317.75):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.86)
                with StaffLayout(number=2):
                    StaffDistance(70.2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=118.5, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.28, default_y=-111.86, dynamics=48.89):
                with Pitch():
                    Step('B')
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
            with Note(default_x=234.82, default_y=-186.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=273.6, default_y=-181.86, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=79.73, default_y=-267.06, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.12, default_y=-257.06, dynamics=41.11):
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
            with Note(default_x=118.5, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=137.89, default_y=-257.06, dynamics=41.11):
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
            with Note(default_x=157.28, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=176.66, default_y=-257.06, dynamics=35.56):
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
            with Note(default_x=196.05, default_y=-287.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.44, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.82, default_y=-242.06, dynamics=41.11):
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
            with Note(default_x=254.21, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.6, default_y=-242.06, dynamics=41.11):
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
            with Note(default_x=292.98, default_y=-252.06, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=292.21):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.57, default_y=-131.86, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.02, default_y=-126.86, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=202.27, default_y=-121.86, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=245.72, default_y=-126.86, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-267.06, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.84, default_y=-257.06, dynamics=41.11):
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
            with Note(default_x=55.57, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=77.3, default_y=-257.06, dynamics=41.11):
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
            with Note(default_x=99.02, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=120.75, default_y=-257.06, dynamics=35.56):
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
            with Note(default_x=150.64, default_y=-272.06, dynamics=41.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.54, default_y=-262.06, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.27, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.99, default_y=-262.06, dynamics=41.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.72, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=267.44, default_y=-262.06, dynamics=35.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=271.61):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.1, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.04, default_y=-111.86, dynamics=48.89):
                with Pitch():
                    Step('B')
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
            with Note(default_x=186.93, default_y=-186.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.88, default_y=-181.86, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-267.06, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.13, default_y=-257.06, dynamics=41.11):
                with Pitch():
                    Step('D')
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
            with Note(default_x=67.1, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=87.07, default_y=-257.06, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.04, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=127.02, default_y=-257.06, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.99, default_y=-267.06, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.96, default_y=-257.06, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.93, default_y=-237.06, dynamics=41.11):
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
            with Note(default_x=206.9, default_y=-257.06, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.88, default_y=-237.06, dynamics=41.11):
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
            with Note(default_x=246.85, default_y=-257.06, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=260.84):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.85, default_y=-146.86, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.9, default_y=-131.86, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=176.0, default_y=-131.86, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.05, default_y=-136.86, dynamics=48.89):
                with Pitch():
                    Step('D')
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
            with Note(default_x=15.8, default_y=-287.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.83, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.85, default_y=-242.06, dynamics=41.11):
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
            with Note(default_x=75.88, default_y=-252.06, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.9, default_y=-242.06, dynamics=41.11):
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
            with Note(default_x=115.93, default_y=-252.06, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.95, default_y=-267.06, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.98, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=176.0, default_y=-237.06, dynamics=41.11):
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
            with Note(default_x=196.03, default_y=-247.06, dynamics=41.11):
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
            with Note(default_x=216.05, default_y=-237.06, dynamics=41.11):
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
            with Note(default_x=236.08, default_y=-247.06, dynamics=35.56):
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
        with Measure(number='30', width=312.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.81)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=117.5, default_y=-131.81, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.26, default_y=-121.81, dynamics=48.89):
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
            with Note(default_x=230.79, default_y=-121.81, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=268.56, default_y=-111.81, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=79.73, default_y=-271.81, dynamics=41.11):
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
            with Note(default_x=98.61, default_y=-261.81, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.5, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.38, default_y=-261.81, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.26, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.14, default_y=-261.81, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=193.03, default_y=-281.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.91, default_y=-261.81, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.79, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.68, default_y=-261.81, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.56, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.44, default_y=-261.81, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=271.67):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=56.04, default_y=-146.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=96.28, default_y=-121.81, dynamics=48.89):
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
            with Note(default_x=186.54, default_y=-121.81, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=226.78, default_y=-126.81, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-281.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.92, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.04, default_y=-236.81, dynamics=41.11):
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
            with Note(default_x=76.16, default_y=-246.81, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.28, default_y=-236.81, dynamics=41.11):
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
            with Note(default_x=116.4, default_y=-246.81, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.52, default_y=-261.81, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.42, default_y=-251.81, dynamics=41.11):
                with Pitch():
                    Step('D')
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
            with Note(default_x=186.54, default_y=-231.81, dynamics=41.11):
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
            with Note(default_x=206.66, default_y=-251.81, dynamics=41.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.78, default_y=-231.81, dynamics=41.11):
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
            with Note(default_x=246.9, default_y=-251.81, dynamics=35.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=229.9):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.16, default_y=-131.81, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.07, default_y=-156.81, dynamics=48.89):
                with Pitch():
                    Step('G')
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
            with Note(default_x=163.1, default_y=-146.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=193.0, default_y=-171.81, dynamics=48.89):
                with Pitch():
                    Step('D')
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
            with Note(default_x=29.26, default_y=-236.81, dynamics=66.67):
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
            with Note(default_x=137.2, default_y=-226.81, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=193.0, default_y=-231.81, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=152.8):
            with Note(default_x=29.33, default_y=-166.81, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=78.28, default_y=-146.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.43, default_y=-146.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=78.28, default_y=-181.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=29.33, default_y=-236.81, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=78.28, default_y=-246.81, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='34', width=175.83):
            with Note(default_x=15.8, default_y=-146.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.2, default_y=-151.81, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.61, default_y=-156.81, dynamics=54.44):
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
            with Note(default_x=95.01, default_y=-181.81, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.01, default_y=-156.81, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=121.42, default_y=-186.81, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.42, default_y=-161.81, dynamics=48.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=147.82, default_y=-191.81, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=147.82, default_y=-166.81, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-176.81, dynamics=60.0):
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
                Duration(360.0)
            with Note(default_x=15.8, default_y=-246.81, dynamics=61.11):
                with Pitch():
                    Step('E')
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
            with Note(default_x=95.01, default_y=-251.81, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=147.82, default_y=-246.81, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=214.09):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.51)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-197.51, dynamics=60.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=83.41, default_y=-172.51, dynamics=60.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=146.66, default_y=-152.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.71, default_y=-152.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=134.79, default_y=-177.51, dynamics=45.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=146.66, default_y=-172.51, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=83.41, default_y=-252.51, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=146.66, default_y=-277.51, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=203.37):
            with Note(default_x=17.23, default_y=-172.51, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-152.51, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=47.08, default_y=-157.51, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.93, default_y=-172.51, dynamics=45.56):
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
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.93, default_y=-162.51, dynamics=56.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=106.77, default_y=-187.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=106.77, default_y=-172.51, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=106.77, default_y=-162.51, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=142.08, default_y=-192.51, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.08, default_y=-177.51, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=142.08, default_y=-167.51, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=171.93, default_y=-197.51, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=171.93, default_y=-172.51, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-182.51, dynamics=60.0):
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
                Duration(360.0)
            with Note(default_x=17.23, default_y=-272.51, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=106.77, default_y=-267.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='37', width=157.08):
            with Note(default_x=15.8, default_y=-197.51, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=15.8, default_y=-187.51, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-172.51, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=66.15, default_y=-197.51, dynamics=51.11):
                with Pitch():
                    Step('G')
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
            with Note(default_x=66.15, default_y=-187.51, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('B')
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
            with Note(default_x=66.15, default_y=-172.51, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=15.8, default_y=-252.51, dynamics=62.22):
                with Pitch():
                    Step('E')
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
            with Note(default_x=66.15, default_y=-252.51, dynamics=62.22):
                with Pitch():
                    Step('E')
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
        with Measure(number='38', width=284.15):
            with Note(default_x=21.88, default_y=-137.51, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.78, default_y=-142.51, dynamics=54.44):
                with Pitch():
                    Step('D')
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
            with Note(default_x=72.37, default_y=-137.51, dynamics=54.44):
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
            with Note(default_x=92.97, default_y=-132.51, dynamics=54.44):
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
            with Note(default_x=113.56, default_y=-127.51, dynamics=54.44):
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
            with Note(default_x=134.99, default_y=-132.51, dynamics=48.89):
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
            with Note(default_x=156.42, default_y=-137.51, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.01, default_y=-142.51, dynamics=54.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.6, default_y=-137.51, dynamics=54.44):
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
            with Note(default_x=218.2, default_y=-132.51, dynamics=54.44):
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
            with Note(default_x=238.79, default_y=-127.51, dynamics=54.44):
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
            with Note(default_x=259.38, default_y=-137.51, dynamics=48.89):
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
            with Backup():
                Duration(720.0)
            with Note(default_x=21.88, default_y=-232.51, dynamics=66.67):
                with Pitch():
                    Step('B')
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
            with Note(default_x=156.42, default_y=-242.51, dynamics=61.11):
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
        with Measure(number='39', width=283.72):
            with Note(default_x=17.23, default_y=-142.51, dynamics=54.44):
                with Pitch():
                    Step('D')
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
            with Note(default_x=38.18, default_y=-137.51, dynamics=54.44):
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
            with Note(default_x=59.13, default_y=-132.51, dynamics=54.44):
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
            with Note(default_x=80.09, default_y=-152.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.98, default_y=-147.51, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=130.93, default_y=-142.51, dynamics=48.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=151.89, default_y=-137.51, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.84, default_y=-132.51, dynamics=54.44):
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
            with Note(default_x=193.79, default_y=-127.51, dynamics=54.44):
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
            with Note(default_x=214.74, default_y=-122.51, dynamics=54.44):
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
            with Note(default_x=238.01, default_y=-117.51, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.96, default_y=-127.51, dynamics=48.89):
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
            with Note(default_x=17.23, default_y=-247.51, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=151.89, default_y=-252.51, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='40', width=422.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.86)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=79.61, default_y=-131.86, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.8, default_y=-126.86, dynamics=54.44):
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
            with Note(default_x=135.98, default_y=-121.86, dynamics=54.44):
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
            with Note(default_x=164.16, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.35, default_y=-111.86, dynamics=54.44):
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
            with Note(default_x=220.53, default_y=-121.86, dynamics=48.89):
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
            with Note(default_x=248.71, default_y=-126.86, dynamics=54.44):
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
            with Note(default_x=276.9, default_y=-121.86, dynamics=54.44):
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
            with Note(default_x=305.08, default_y=-116.86, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.26, default_y=-151.86, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.16, default_y=-146.86, dynamics=54.44):
                with Pitch():
                    Step('C')
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
            with Note(default_x=393.06, default_y=-141.86, dynamics=48.89):
                with Pitch():
                    Step('D')
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
            with Note(default_x=79.61, default_y=-246.86, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=248.71, default_y=-241.86, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=363.16, default_y=-236.86, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=286.2):
            with Note(default_x=23.46, default_y=-136.86, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.61, default_y=-146.86, dynamics=54.44):
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
            with Note(default_x=67.75, default_y=-151.86, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.9, default_y=-156.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.04, default_y=-161.86, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.18, default_y=-166.86, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.33, default_y=-171.86, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=23.46, default_y=-241.86, dynamics=66.67):
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
            with Note(default_x=156.33, default_y=-231.86, dynamics=61.11):
                with Pitch():
                    Step('B')
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
        with Measure(number='42', width=194.25):
            with Note(default_x=15.8, default_y=-186.86, dynamics=63.33):
                with Pitch():
                    Step('B')
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
            with Note(default_x=15.8, default_y=-176.86, dynamics=63.33):
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
            with Note(default_x=15.8, default_y=-166.86, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=110.54, default_y=-181.86, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
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
            with Note(default_x=110.54, default_y=-171.86, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=122.41, default_y=-166.86, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-266.86, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=110.54, default_y=-271.86, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
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
        with Measure(number='43', width=239.12):
            with Note(default_x=25.94, default_y=-186.86, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=25.94, default_y=-176.86, dynamics=51.11):
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
            with Note(default_x=25.94, default_y=-166.86, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=123.84, default_y=-186.86, dynamics=45.56):
                with Pitch():
                    Step('B')
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
            with Note(default_x=123.84, default_y=-171.86, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=123.84, default_y=-161.86, dynamics=61.11):
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
            with Note(default_x=25.94, default_y=-266.86, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=123.84, default_y=-251.86, dynamics=54.44):
                with Pitch():
                    Step('E')
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
        with Measure(number='44', width=296.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.19)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=83.41, default_y=-172.19, dynamics=51.11):
                with Pitch():
                    Step('B')
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
            with Note(default_x=83.41, default_y=-162.19, dynamics=51.11):
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
            with Note(default_x=83.41, default_y=-152.19, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=196.89, default_y=-167.19, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
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
            with Note(default_x=196.89, default_y=-157.19, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=208.75, default_y=-152.19, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=83.41, default_y=-252.19, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=196.89, default_y=-257.19, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
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
        with Measure(number='45', width=248.46):
            with Note(default_x=21.03, default_y=-172.19, dynamics=63.33):
                with Pitch():
                    Step('B')
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
            with Note(default_x=21.03, default_y=-162.19, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-152.19, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=21.03, default_y=-252.19, dynamics=60.0):
                with Pitch():
                    Step('B')
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
            with Note():
                Rest()
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='46', width=287.32):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=60.66, default_y=-172.19, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.53, default_y=-157.19, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=195.26, default_y=-157.19, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.12, default_y=-162.19, dynamics=48.89):
                with Pitch():
                    Step('D')
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
            with Note(default_x=15.8, default_y=-272.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.23, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.66, default_y=-227.19, dynamics=41.11):
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
            with Note(default_x=83.1, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.53, default_y=-227.19, dynamics=41.11):
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
            with Note(default_x=127.96, default_y=-237.19, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.39, default_y=-252.19, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.83, default_y=-232.19, dynamics=41.11):
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
            with Note(default_x=195.26, default_y=-222.19, dynamics=41.11):
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
            with Note(default_x=217.69, default_y=-232.19, dynamics=41.11):
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
            with Note(default_x=240.12, default_y=-222.19, dynamics=41.11):
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
            with Note(default_x=262.56, default_y=-232.19, dynamics=35.56):
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
        with Measure(number='47', width=309.8):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=77.82, default_y=-157.19, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.87, default_y=-147.19, dynamics=48.89):
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
            with Note(default_x=215.96, default_y=-147.19, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=262.01, default_y=-137.19, dynamics=48.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.77, default_y=-262.19, dynamics=41.11):
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
            with Note(default_x=54.79, default_y=-252.19, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.82, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.84, default_y=-252.19, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.87, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.89, default_y=-252.19, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=169.91, default_y=-272.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=192.94, default_y=-252.19, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.96, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.99, default_y=-252.19, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.01, default_y=-237.19, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.04, default_y=-252.19, dynamics=35.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=380.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(100.88)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.3, default_y=-195.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=173.18, default_y=-180.88, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=262.95, default_y=-180.88, dynamics=45.56):
                with Pitch():
                    Step('E')
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
            with Note(default_x=262.95, default_y=-170.88, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=345.94, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=307.83, default_y=-185.88, dynamics=40.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=307.83, default_y=-175.88, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=83.41, default_y=-295.88, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.85, default_y=-260.88, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.3, default_y=-250.88, dynamics=41.11):
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
            with Note(default_x=150.74, default_y=-260.88, dynamics=41.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.18, default_y=-250.88, dynamics=41.11):
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
            with Note(default_x=195.62, default_y=-260.88, dynamics=35.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.06, default_y=-275.88, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=240.5, default_y=-240.88, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.95, default_y=-275.88, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.39, default_y=-240.88, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.83, default_y=-275.88, dynamics=41.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.27, default_y=-245.88, dynamics=35.56):
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
        with Measure(number='49', width=204.81):
            with Note(default_x=31.81, default_y=-125.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.94, default_y=-130.88, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.08, default_y=-135.88, dynamics=54.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=122.22, default_y=-145.88, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=122.22, default_y=-135.88, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=158.57, default_y=-145.88, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=170.43, default_y=-140.88, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.81, default_y=-250.88, dynamics=66.67):
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
            with Note(default_x=122.22, default_y=-240.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.43, default_y=-245.88, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='50', width=186.97):
            with Note(default_x=31.81, default_y=-145.88, dynamics=48.89):
                with Pitch():
                    Step('E')
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
            with Note(default_x=97.64, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=151.63, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=97.64, default_y=-195.88, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=97.64, default_y=-180.88, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=31.81, default_y=-250.88, dynamics=55.56):
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
            with Note(default_x=97.64, default_y=-285.88, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='51', width=205.36):
            with Note(default_x=15.8, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.13, default_y=-165.88, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.45, default_y=-170.88, dynamics=54.44):
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
            with Note(default_x=109.78, default_y=-170.88, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=141.11, default_y=-175.88, dynamics=48.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.43, default_y=-180.88, dynamics=54.44):
                with Pitch():
                    Step('E')
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
            with Note(default_x=15.8, default_y=-190.88, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-180.88, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=109.78, default_y=-185.88, dynamics=54.44):
                with Pitch():
                    Step('D')
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
            with Note(default_x=15.8, default_y=-280.88, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=109.78, default_y=-240.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=141.11, default_y=-245.88, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=172.43, default_y=-250.88, dynamics=54.44):
                with Pitch():
                    Step('G')
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
        with Measure(number='52', width=164.95):
            with Note(default_x=13.09, default_y=-180.88, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=89.58, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=134.98, default_y=-160.88, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=13.09, default_y=-250.88, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=89.58, default_y=-260.88, dynamics=61.11):
                with Pitch():
                    Step('E')
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
        with Measure(number='53', width=733.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.45)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.65, default_y=-155.45, dynamics=45.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.52, default_y=-150.45, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=162.53, default_y=-160.45, dynamics=40.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.53, default_y=-145.45, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=233.41, default_y=-165.45, dynamics=45.56):
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
            with Note(default_x=233.41, default_y=-140.45, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=304.29, default_y=-165.45, dynamics=45.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=304.29, default_y=-140.45, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=485.77, default_y=-145.45, dynamics=45.56):
                with Pitch():
                    Step('D')
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
            with Note(default_x=523.65, default_y=-140.45, dynamics=61.11):
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
                Beam('begin', number=4)
            with Note(default_x=547.33, default_y=-145.45, dynamics=45.56):
                with Pitch():
                    Step('D')
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
            with Note(default_x=571.01, default_y=-140.45, dynamics=61.11):
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
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=608.9, default_y=-145.45, dynamics=40.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=661.0, default_y=-175.45, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=661.0, default_y=-140.45, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=485.77, default_y=-170.45, dynamics=54.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=91.65, default_y=-255.45, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.41, default_y=-230.45, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=304.29, default_y=-235.45, dynamics=54.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=485.77, default_y=-240.45, dynamics=48.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=661.0, default_y=-245.45, dynamics=54.44):
                with Pitch():
                    Step('G')
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
        with Measure(number='54', width=408.94):
            with Note(default_x=14.21, default_y=-175.45, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=14.21, default_y=-140.45, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
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
            with Note(default_x=14.21, default_y=-245.45, dynamics=66.67):
                with Pitch():
                    Step('G')
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