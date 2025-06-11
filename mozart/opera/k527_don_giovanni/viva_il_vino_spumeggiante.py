with ScorePartwise(version='3.1'):
    with Identification():
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
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.25)
            PageWidth(1190.8)
            with PageMargins(type='even'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Viva il vino spumeggiante', default_x=595.402, default_y=1626.56, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('O du eselhafter Peierl KV 560', default_x=595.402, default_y=1569.88, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W.A. Mozart', default_x=1134.12, default_y=1526.56, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
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
    with Part(id='P1'):
        with Measure(number='1', width=313.42):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(87.6)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='cut'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=99.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=153.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=182.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=209.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=239.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=276.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='2', width=108.65):
            with Note(default_x=23.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=54.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='3', width=225.29):
            with Note(default_x=18.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=72.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=107.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=137.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=166.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=196.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='4', width=184.72):
            with Note(default_x=18.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=48.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=121.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=150.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='5', width=157.76):
            with Note(default_x=19.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=71.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=94.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=123.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='6', width=239.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(100.72)
            with Note(default_x=77.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=186.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=212.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='7', width=230.13):
            with Note(default_x=31.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=80.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=129.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=179.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='8', width=296.92):
            with Note(default_x=16.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=51.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=86.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=121.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=155.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=190.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=225.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=260.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='9', width=278.87):
            with Note(default_x=16.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=70.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=396.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(100.72)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=156.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=196.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=236.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=275.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=315.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=354.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='11', width=316.82):
            with Note(default_x=18.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=81.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='12', width=332.38):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=96.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=135.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=174.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='13', width=313.42):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=104.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=132.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=161.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=195.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-55.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='14', width=269.44):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=83.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=113.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=144.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=1.81, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=175.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=206.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=237.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='15', width=190.08):
            with Note(default_x=31.22, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=110.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='16', width=272.49):
            with Note(default_x=19.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=208.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=239.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='17', width=391.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(132.7)
            with Note(default_x=77.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=184.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=225.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=266.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=307.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=348.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='18', width=336.19):
            with Note(default_x=23.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=256.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=295.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='19', width=318.23):
            with Note(default_x=18.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=120.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=159.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=198.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=238.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=277.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.37, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='20', width=317.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(132.7)
            with Note(default_x=77.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=197.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='21', width=259.55):
            with Note(default_x=19.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=139.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='22', width=273.83):
            with Note(default_x=19.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=146.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=178.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='23', width=194.48):
            with Note(default_x=31.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='24', width=374.5):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=335.45):
            with Note(default_x=19.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Il', font_family='Times New Roman')
            with Note(default_x=85.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'uo", font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('moaf', font_family='Times New Roman')
        with Measure(number='26', width=335.48):
            with Note(default_x=23.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=84.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.85, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.', font_family='Times New Roman')
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
            with Note(default_x=296.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('se', font_family='Times New Roman')
        with Measure(number='27', width=384.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(93.42)
            with Note(default_x=77.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.92, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('pur,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=181.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('lor,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=342.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman')
        with Measure(number='28', width=338.77):
            with Note(default_x=19.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta', font_family='Times New Roman')
            with Note(default_x=82.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=183.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=260.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='29', width=322.22):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=170.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=245.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='30', width=412.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(93.42)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=244.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='31', width=275.11):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=91.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='32', width=357.52):
            with Note(default_x=19.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='33', width=397.52):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=270.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=312.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='34', width=339.79):
            with Note(default_x=23.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='35', width=308.13):
            with Note(default_x=20.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=117.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=192.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=230.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=269.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='36', width=330.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(118.72)
            with Note(default_x=77.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=237.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=266.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=295.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.51, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='37', width=255.39):
            with Note(default_x=19.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=164.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=191.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=220.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='38', width=269.68):
            with Note(default_x=19.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=175.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='39', width=190.32):
            with Note(default_x=31.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='40', width=383.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(118.72)
            with Note(default_x=80.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=118.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=155.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=193.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=231.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=268.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=306.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=344.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='41', width=319.17):
            with Note(default_x=16.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=79.82, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='42', width=343.05):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=110.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=148.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=1.68, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=187.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=225.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=264.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=302.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='43', width=376.86):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=140.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='44', width=342.06):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=106.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=145.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=183.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='45', width=326.51):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=95.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=134.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=171.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='46', width=412.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(135.17)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=119.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=161.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=202.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=244.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=286.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='47', width=275.11):
            with Note(default_x=31.22, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='48', width=357.52):
            with Note(default_x=19.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=229.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='49', width=391.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(135.17)
            with Note(default_x=77.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=184.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=225.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=266.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=307.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=348.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='50', width=336.19):
            with Note(default_x=23.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=256.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=295.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='51', width=318.23):
            with Note(default_x=18.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=120.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=159.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=198.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=238.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=277.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.37, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='52', width=317.57):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=197.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='53', width=259.55):
            with Note(default_x=19.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=139.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='54', width=273.83):
            with Note(default_x=19.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=146.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=178.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='55', width=194.48):
            with Note(default_x=31.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='56', width=374.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(104.49)
            with Note(default_x=77.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='57', width=335.45):
            with Note(default_x=19.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Il', font_family='Times New Roman')
            with Note(default_x=85.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'uo", font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('moaf', font_family='Times New Roman')
        with Measure(number='58', width=335.48):
            with Note(default_x=23.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=84.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.85, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.', font_family='Times New Roman')
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
            with Note(default_x=296.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('se', font_family='Times New Roman')
        with Measure(number='59', width=384.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(104.49)
            with Note(default_x=77.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.92, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('pur,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=181.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('lor,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=342.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman')
        with Measure(number='60', width=338.77):
            with Note(default_x=19.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta', font_family='Times New Roman')
            with Note(default_x=82.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=183.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=260.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='61', width=322.22):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=170.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=245.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='62', width=412.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=244.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='63', width=275.11):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=91.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='64', width=357.52):
            with Note(default_x=19.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='65', width=397.52):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(104.12)
            with Note(default_x=77.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=270.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=312.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='66', width=339.79):
            with Note(default_x=23.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='67', width=308.13):
            with Note(default_x=20.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=117.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=192.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=230.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=269.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='68', width=330.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    SystemDistance(104.12)
            with Note(default_x=77.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=237.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=266.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=295.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.51, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='69', width=255.39):
            with Note(default_x=19.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=164.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=191.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=220.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='70', width=269.68):
            with Note(default_x=19.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=175.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='71', width=190.32):
            with Note(default_x=31.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='72', width=185.6):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(32.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
        with Measure(number='73', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='74', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='75', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='76', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='77', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='78', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='79', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='80', width=114.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=313.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(66.45)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='cut'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=108.65):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=225.29):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=184.72):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=157.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=239.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=230.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='8', width=296.92):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='9', width=278.87):
            with Note(default_x=16.42, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=103.83, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=137.45, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=171.07, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=204.7, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=242.09, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='10', width=396.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note(default_x=77.5, default_y=-131.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=156.78, default_y=-141.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=316.82):
            with Note(default_x=18.62, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=120.09, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=159.12, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=198.14, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=237.17, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=276.2, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='12', width=332.38):
            with Note(default_x=18.42, default_y=-131.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=96.51, default_y=-141.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=213.64, default_y=-141.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=252.69, default_y=-141.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=291.73, default_y=-141.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='13', width=313.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.5)
            with Note(default_x=77.38, default_y=-128.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=222.68, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=249.84, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=278.84, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='14', width=269.44):
            with Note(default_x=19.06, default_y=-133.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=175.51, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=206.29, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=237.06, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='15', width=190.08):
            with Note(default_x=31.22, default_y=-148.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-128.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=110.97, default_y=-133.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=149.73, default_y=-158.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='16', width=272.49):
            with Note(default_x=19.47, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=50.9, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=82.32, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=113.75, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=145.18, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=176.61, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=208.03, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=239.46, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='17', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.38, default_y=-151.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=143.07, default_y=-161.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=336.19):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.66, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=101.51, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=140.36, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=179.21, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=218.05, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=256.9, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=295.75, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='19', width=318.23):
            with Note(default_x=18.62, default_y=-151.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=81.36, default_y=-161.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='20', width=317.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.75)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=105.76, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=163.02, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=197.11, default_y=-136.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='21', width=259.55):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.73, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=75.99, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=104.99, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=139.08, default_y=-131.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-55.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='22', width=273.83):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.82, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=83.82, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=115.22, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=146.62, default_y=-136.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=178.03, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-156.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='23', width=194.48):
            with Note(default_x=31.22, default_y=-166.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-166.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='24', width=374.5):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.8)
            with Note(default_x=77.38, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-51.2):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=262.22, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=299.11, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=336.01, default_y=-137.8):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='25', width=335.45):
            with Note(default_x=19.62, default_y=-132.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-152.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=209.81, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=251.15, default_y=-162.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-152.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='26', width=335.48):
            with Note(default_x=23.46, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.13, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=258.71, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=296.3, default_y=-137.8):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='27', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.95)
            with Note(default_x=77.38, default_y=-150.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=181.88, default_y=-160.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-170.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=262.26, default_y=-160.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=302.45, default_y=-180.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=342.65, default_y=-170.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='28', width=338.77):
            with Note(default_x=19.42, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=182.75, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='29', width=322.22):
            with Note(default_x=19.47, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.76, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=169.68, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='30', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.94)
            with Note(default_x=77.74, default_y=-117.94):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=161.1, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=244.47, default_y=-132.94):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=286.15, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-152.94):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-157.94):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='31', width=275.11):
            with Note(default_x=31.22, default_y=-162.94):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-132.94):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-147.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='32', width=357.52):
            with Note(default_x=19.11, default_y=-152.94):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='33', width=397.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.45)
            with Note(default_x=77.38, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Il', font_family='Times New Roman')
            with Note(default_x=144.44, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-135.45):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-130.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'uo", font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('moaf', font_family='Times New Roman')
        with Measure(number='34', width=339.79):
            with Note(default_x=23.82, default_y=-145.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=85.74, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-135.45):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.85, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.', font_family='Times New Roman')
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
            with Note(default_x=300.08, default_y=-145.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('se', font_family='Times New Roman')
        with Measure(number='35', width=308.13):
            with Note(default_x=20.08, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.92, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('pur,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.56, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-130.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('lor,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=269.03, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman')
        with Measure(number='36', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.3)
            with Note(default_x=77.5, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta', font_family='Times New Roman')
            with Note(default_x=124.73, default_y=-139.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-134.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=2.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=208.25, default_y=-124.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=266.38, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='37', width=255.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=137.37, default_y=-119.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=191.81, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='38', width=269.68):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=144.84, default_y=-124.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='39', width=190.32):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=72.21, default_y=-139.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-134.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-129.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='40', width=383.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.75)
            with Note(default_x=80.34, default_y=-137.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='41', width=319.17):
            with Note(default_x=16.42, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=119.44, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=159.07, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=198.69, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=238.32, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=277.94, default_y=-127.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='42', width=343.05):
            with Note(default_x=23.82, default_y=-137.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=110.44, default_y=-147.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='43', width=376.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.3)
            with Note(default_x=77.38, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=179.29, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=218.48, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=257.68, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=296.87, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=336.07, default_y=-120.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='44', width=342.06):
            with Note(default_x=18.42, default_y=-130.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=106.25, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=223.35, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=262.39, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=301.42, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='45', width=326.51):
            with Note(default_x=19.11, default_y=-115.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=210.37, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=248.55, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=286.73, default_y=-140.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='46', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.5)
            with Note(default_x=77.38, default_y=-133.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=286.15, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-143.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='47', width=275.11):
            with Note(default_x=31.22, default_y=-148.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-128.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-133.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-158.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='48', width=357.52):
            with Note(default_x=19.47, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=61.53, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=103.58, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=145.64, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=187.69, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=229.75, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-153.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='49', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.38, default_y=-151.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=143.07, default_y=-161.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='50', width=336.19):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.66, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=101.51, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=140.36, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=179.21, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=218.05, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=256.9, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=295.75, default_y=-146.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='51', width=318.23):
            with Note(default_x=18.62, default_y=-151.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=81.36, default_y=-161.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='52', width=317.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.75)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=105.76, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=163.02, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=197.11, default_y=-136.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='53', width=259.55):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=47.73, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=75.99, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=104.99, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=139.08, default_y=-131.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-55.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='54', width=273.83):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.82, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=83.82, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=115.22, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=146.62, default_y=-136.75):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=178.03, default_y=-146.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-156.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='55', width=194.48):
            with Note(default_x=31.22, default_y=-166.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-166.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-161.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='56', width=374.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.8)
            with Note(default_x=77.38, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-51.2):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=262.22, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=299.11, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=336.01, default_y=-137.8):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='57', width=335.45):
            with Note(default_x=19.62, default_y=-132.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-152.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=209.81, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=251.15, default_y=-162.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-152.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='58', width=335.48):
            with Note(default_x=23.46, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.13, default_y=-147.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=258.71, default_y=-142.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=296.3, default_y=-137.8):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='59', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.95)
            with Note(default_x=77.38, default_y=-150.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=181.88, default_y=-160.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-170.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=262.26, default_y=-160.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=302.45, default_y=-180.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=342.65, default_y=-170.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='60', width=338.77):
            with Note(default_x=19.42, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=182.75, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='61', width=322.22):
            with Note(default_x=19.47, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.76, default_y=-165.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=169.68, default_y=-130.95):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='62', width=412.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.94)
            with Note(default_x=77.74, default_y=-117.94):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=161.1, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=244.47, default_y=-132.94):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=286.15, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-152.94):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-157.94):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='63', width=275.11):
            with Note(default_x=31.22, default_y=-162.94):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-132.94):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-142.94):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-147.94):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='64', width=357.52):
            with Note(default_x=19.11, default_y=-152.94):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='65', width=397.52):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.45)
            with Note(default_x=77.38, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Il', font_family='Times New Roman')
            with Note(default_x=144.44, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-135.45):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-130.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'uo", font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('moaf', font_family='Times New Roman')
        with Measure(number='66', width=339.79):
            with Note(default_x=23.82, default_y=-145.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=85.74, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-135.45):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.85, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.', font_family='Times New Roman')
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
            with Note(default_x=300.08, default_y=-145.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('se', font_family='Times New Roman')
        with Measure(number='67', width=308.13):
            with Note(default_x=20.08, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.92, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('pur,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.56, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-130.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('lor,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=269.03, default_y=-140.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman')
        with Measure(number='68', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.3)
            with Note(default_x=77.5, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta', font_family='Times New Roman')
            with Note(default_x=124.73, default_y=-139.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-134.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=2.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=208.25, default_y=-124.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=266.38, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='69', width=255.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=137.37, default_y=-119.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=191.81, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='70', width=269.68):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=144.84, default_y=-124.3):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-144.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='71', width=190.32):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=72.21, default_y=-139.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-134.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-129.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='72', width=185.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=77.38, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.61, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
        with Measure(number='73', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='74', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='75', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='76', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='77', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='78', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='79', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='80', width=114.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=313.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='cut'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=108.65):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=225.29):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=184.72):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=157.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=239.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.45)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=230.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='8', width=296.92):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='9', width=278.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='10', width=396.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.45)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='11', width=316.82):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='12', width=332.38):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='13', width=313.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='14', width=269.44):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='15', width=190.08):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='16', width=272.49):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='17', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note(default_x=77.38, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=184.12, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=225.18, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=266.24, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=307.29, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=348.35, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='18', width=336.19):
            with Note(default_x=23.82, default_y=-242.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=101.51, default_y=-252.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='19', width=318.23):
            with Note(default_x=18.62, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=120.57, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=159.78, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=198.99, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=238.2, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=277.42, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='20', width=317.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.5)
            with Note(default_x=77.5, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=225.73, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=253.99, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=282.99, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='21', width=259.55):
            with Note(default_x=19.11, default_y=-240.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=167.7, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=195.97, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=224.96, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='22', width=273.83):
            with Note(default_x=19.06, default_y=-245.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.03, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='23', width=194.48):
            with Note(default_x=31.22, default_y=-260.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-240.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-245.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-270.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='24', width=374.5):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.74, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=114.63, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=151.53, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=188.43, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=225.32, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=262.22, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=299.11, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=336.01, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='25', width=335.45):
            with Note(default_x=19.62, default_y=-264.2):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=85.77, default_y=-274.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=335.48):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=61.4, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=145.97, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=183.55, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=221.13, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=258.71, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=296.3, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='27', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.95)
            with Note(default_x=77.38, default_y=-288.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=141.69, default_y=-298.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='28', width=338.77):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.93, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=144.59, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=182.75, default_y=-273.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='29', width=322.22):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.11, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=94.76, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=132.4, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=169.68, default_y=-268.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='30', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.44)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=119.42, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=161.1, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=202.78, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=244.47, default_y=-248.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=286.15, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-268.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='31', width=275.11):
            with Note(default_x=31.22, default_y=-278.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-278.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='32', width=357.52):
            with Note(default_x=19.11, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=229.75, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-253.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-248.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='33', width=397.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.8)
            with Note(default_x=77.38, default_y=-243.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=270.18, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=312.09, default_y=-273.25):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='34', width=339.79):
            with Note(default_x=23.46, default_y=-258.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=223.87, default_y=-258.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=261.97, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=300.08, default_y=-248.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='35', width=308.13):
            with Note(default_x=20.08, default_y=-243.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=117.56, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=192.54, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=230.04, default_y=-273.25):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=269.03, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='36', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.55)
            with Note(default_x=77.5, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=207.89, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='37', width=255.39):
            with Note(default_x=19.47, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.92, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=137.01, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='38', width=269.68):
            with Note(default_x=19.42, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.22, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=144.84, default_y=-253.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=175.65, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-278.85):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='39', width=190.32):
            with Note(default_x=31.22, default_y=-283.85):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-258.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-268.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='40', width=383.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.45)
            with Note(default_x=80.34, default_y=-258.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='41', width=319.17):
            with Note(default_x=16.42, default_y=-253.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Il', font_family='Times New Roman')
            with Note(default_x=79.82, default_y=-253.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note(default_x=119.44, default_y=-248.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=159.07, default_y=-243.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'uo", font_family='Times New Roman')
            with Note(default_x=277.94, default_y=-253.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('moaf', font_family='Times New Roman')
        with Measure(number='42', width=343.05):
            with Note(default_x=23.82, default_y=-258.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=86.38, default_y=-253.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=110.44, default_y=-248.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.85, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.', font_family='Times New Roman')
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
            with Note(default_x=302.95, default_y=-258.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('se', font_family='Times New Roman')
        with Measure(number='43', width=376.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.0)
            with Note(default_x=77.38, default_y=-248.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.92, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('pur,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=179.29, default_y=-248.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta', font_family='Times New Roman')
            with Note(default_x=218.48, default_y=-238.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('lor,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=336.07, default_y=-248.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman')
        with Measure(number='44', width=342.06):
            with Note(default_x=18.42, default_y=-253.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta', font_family='Times New Roman')
            with Note(default_x=81.85, default_y=-248.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=106.25, default_y=-243.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=184.32, default_y=-233.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=262.39, default_y=-253.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='45', width=326.51):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=172.19, default_y=-228.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=248.55, default_y=-253.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='46', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=244.47, default_y=-242.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-262.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='47', width=275.11):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=91.79, default_y=-257.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-252.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-247.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='48', width=357.52):
            with Note(default_x=19.11, default_y=-252.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-47.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='49', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note(default_x=77.38, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=184.12, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=225.18, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=266.24, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=307.29, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=348.35, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='50', width=336.19):
            with Note(default_x=23.82, default_y=-242.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=101.51, default_y=-252.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='51', width=318.23):
            with Note(default_x=18.62, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=120.57, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=159.78, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=198.99, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=238.2, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=277.42, default_y=-232.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='52', width=317.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.5)
            with Note(default_x=77.5, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=134.02, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.65, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=225.73, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=253.99, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=282.99, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='53', width=259.55):
            with Note(default_x=19.11, default_y=-240.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=167.7, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=195.97, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=224.96, default_y=-265.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='54', width=273.83):
            with Note(default_x=19.06, default_y=-245.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.03, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=209.43, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=240.83, default_y=-255.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='55', width=194.48):
            with Note(default_x=31.22, default_y=-260.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-240.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=112.43, default_y=-245.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=152.65, default_y=-270.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='56', width=374.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.74, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=114.63, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=151.53, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=188.43, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=225.32, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=262.22, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=299.11, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=336.01, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='57', width=335.45):
            with Note(default_x=19.62, default_y=-264.2):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=85.77, default_y=-274.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-46.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='58', width=335.48):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=61.4, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=145.97, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=183.55, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=221.13, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=258.71, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=296.3, default_y=-259.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='59', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.95)
            with Note(default_x=77.38, default_y=-288.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=141.69, default_y=-298.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='60', width=338.77):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.93, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=144.59, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=182.75, default_y=-273.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='61', width=322.22):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=57.11, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=94.76, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=132.4, default_y=-283.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=169.68, default_y=-268.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='62', width=412.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.44)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=119.42, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=161.1, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=202.78, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=244.47, default_y=-248.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=286.15, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-268.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='63', width=275.11):
            with Note(default_x=31.22, default_y=-278.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-278.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-273.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='64', width=357.52):
            with Note(default_x=19.11, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.57, default_y=-55.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=229.75, default_y=-258.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bi', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-253.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('slac', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-248.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ca', font_family='Times New Roman')
        with Measure(number='65', width=397.52):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.8)
            with Note(default_x=77.38, default_y=-243.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("l'ac", font_family='Times New Roman')
            with Note(default_x=186.35, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua,', font_family='Times New Roman')
            with Note(default_x=228.26, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('siac', font_family='Times New Roman')
            with Note(default_x=270.18, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('qua', font_family='Times New Roman')
            with Note(default_x=312.09, default_y=-273.25):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("l'in", font_family='Times New Roman')
            with Note(default_x=354.0, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te', font_family='Times New Roman')
        with Measure(number='66', width=339.79):
            with Note(default_x=23.46, default_y=-258.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.74, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('stin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=223.87, default_y=-258.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel', font_family='Times New Roman')
            with Note(default_x=261.97, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'a", font_family='Times New Roman')
            with Note(default_x=300.08, default_y=-248.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman')
        with Measure(number='67', width=308.13):
            with Note(default_x=20.08, default_y=-243.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rar', font_family='Times New Roman')
            with Note(default_x=117.56, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('siin', font_family='Times New Roman')
            with Note(default_x=155.05, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman')
            with Note(default_x=192.54, default_y=-253.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la', font_family='Times New Roman')
            with Note(default_x=230.04, default_y=-273.25):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ghet', font_family='Times New Roman')
            with Note(default_x=269.03, default_y=-263.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-51.2):
                    Syllabic('end')
                    Text('toal', font_family='Times New Roman')
        with Measure(number='68', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.55)
            with Note(default_x=77.5, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pin', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Can', font_family='Times New Roman')
            with Note(default_x=207.89, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tiam,', font_family='Times New Roman')
        with Measure(number='69', width=255.39):
            with Note(default_x=19.47, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.92, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
            with Note(default_x=137.01, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman')
        with Measure(number='70', width=269.68):
            with Note(default_x=19.42, default_y=-238.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.22, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=144.84, default_y=-253.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tia', font_family='Times New Roman')
            with Note(default_x=175.65, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-273.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-278.85):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='71', width=190.32):
            with Note(default_x=31.22, default_y=-283.85):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-258.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-263.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-268.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='72', width=185.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=77.38, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.61, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
        with Measure(number='73', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='74', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='75', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='76', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='77', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='78', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='79', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='80', width=114.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=313.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='cut'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=108.65):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=225.29):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=184.72):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=157.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=239.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=230.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='8', width=296.92):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='9', width=278.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='10', width=396.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='11', width=316.82):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='12', width=332.38):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='13', width=313.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='14', width=269.44):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='15', width=190.08):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='16', width=272.49):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='17', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.45)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='18', width=336.19):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=318.23):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=317.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='21', width=259.55):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=273.83):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=194.48):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=374.5):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.82)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=335.45):
            with Note(default_x=19.62, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=209.81, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=251.15, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='26', width=335.48):
            with Note(default_x=23.82, default_y=-341.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-351.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='27', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.03)
            with Note(default_x=77.38, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=181.88, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=262.26, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=302.45, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=342.65, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='28', width=338.77):
            with Note(default_x=19.42, default_y=-367.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.62, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=260.14, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=298.66, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='29', width=322.22):
            with Note(default_x=19.11, default_y=-352.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.69, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=245.33, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=282.98, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='30', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.02)
            with Note(default_x=77.38, default_y=-347.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=286.15, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='31', width=275.11):
            with Note(default_x=31.22, default_y=-362.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-342.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-347.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-372.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='32', width=357.52):
            with Note(default_x=19.47, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=61.53, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=103.58, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=145.64, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=187.69, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=229.75, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='33', width=397.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.38, default_y=-349.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=144.44, default_y=-359.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-40.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='34', width=339.79):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=61.92, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=147.66, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.08, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=185.76, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=223.87, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=261.97, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=300.08, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='35', width=308.13):
            with Note(default_x=20.08, default_y=-349.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=80.07, default_y=-359.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='36', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.05)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.56, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=173.79, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.51, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=207.89, default_y=-352.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-53.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='37', width=255.39):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=46.69, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=73.92, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=102.92, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=137.01, default_y=-347.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-53.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='38', width=269.68):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.23, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=83.22, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=114.03, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=144.84, default_y=-352.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=1.77, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=175.65, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-372.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='39', width=190.32):
            with Note(default_x=31.22, default_y=-382.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-382.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='40', width=383.21):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=77.38, default_y=-338.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=12.25, default_y=-40.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
        with Measure(number='41', width=319.17):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=343.05):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='43', width=376.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.7)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='44', width=342.06):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='45', width=326.51):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='46', width=412.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='47', width=275.11):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='48', width=357.52):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='49', width=391.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.45)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='50', width=336.19):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='51', width=318.23):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='52', width=317.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='53', width=259.55):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='54', width=273.83):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='55', width=194.48):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='56', width=374.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.82)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='57', width=335.45):
            with Note(default_x=19.62, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vi', font_family='Times New Roman')
            with Note(default_x=127.12, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=168.46, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=209.81, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=251.15, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('spu', font_family='Times New Roman')
            with Note(default_x=292.5, default_y=-331.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('meg', font_family='Times New Roman')
        with Measure(number='58', width=335.48):
            with Note(default_x=23.82, default_y=-341.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gian', font_family='Times New Roman')
            with Note(default_x=108.37, default_y=-351.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('te.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='59', width=384.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.03)
            with Note(default_x=77.38, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('nel', font_family='Times New Roman')
            with Note(default_x=181.88, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bic', font_family='Times New Roman')
            with Note(default_x=222.07, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('chie', font_family='Times New Roman')
            with Note(default_x=262.26, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=302.45, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scin', font_family='Times New Roman')
            with Note(default_x=342.65, default_y=-357.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('til', font_family='Times New Roman')
        with Measure(number='60', width=338.77):
            with Note(default_x=19.42, default_y=-367.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lan', font_family='Times New Roman')
            with Note(default_x=106.08, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.65, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.62, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=260.14, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=298.66, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='61', width=322.22):
            with Note(default_x=19.11, default_y=-352.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.69, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=245.33, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=282.98, default_y=-377.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='62', width=412.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.02)
            with Note(default_x=77.38, default_y=-347.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=286.15, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ba', font_family='Times New Roman')
            with Note(default_x=327.83, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=369.51, default_y=-357.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo', font_family='Times New Roman')
        with Measure(number='63', width=275.11):
            with Note(default_x=31.22, default_y=-362.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chian', font_family='Times New Roman')
            with Note(default_x=91.79, default_y=-342.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tio', font_family='Times New Roman')
            with Note(default_x=152.36, default_y=-347.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gri', font_family='Times New Roman')
            with Note(default_x=212.94, default_y=-372.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gno', font_family='Times New Roman')
        with Measure(number='64', width=357.52):
            with Note(default_x=19.47, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lin,', font_family='Times New Roman')
            with Note(default_x=61.53, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=103.58, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=145.64, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=187.69, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=229.75, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
            with Note(default_x=271.81, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=313.86, default_y=-367.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ne', font_family='Times New Roman')
        with Measure(number='65', width=397.52):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.4)
            with Note(default_x=77.38, default_y=-349.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ro', font_family='Times New Roman')
            with Note(default_x=144.44, default_y=-359.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.2, default_y=-40.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('so,', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='66', width=339.79):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=61.92, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
            with Note(default_x=109.55, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sciut', font_family='Times New Roman')
            with Note(default_x=147.66, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.08, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('toa', font_family='Times New Roman')
            with Note(default_x=185.76, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma', font_family='Times New Roman')
            with Note(default_x=223.87, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bi', font_family='Times New Roman')
            with Note(default_x=261.97, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=300.08, default_y=-344.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu', font_family='Times New Roman')
        with Measure(number='67', width=308.13):
            with Note(default_x=20.08, default_y=-349.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sto', font_family='Times New Roman')
            with Note(default_x=80.07, default_y=-359.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('so', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='68', width=330.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.05)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.56, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=144.73, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=173.79, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.51, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=207.89, default_y=-352.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-53.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='69', width=255.39):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=46.69, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman')
            with Note(default_x=73.92, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=102.92, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
            with Note(default_x=137.01, default_y=-347.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.29, default_y=-53.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('vin,', font_family='Times New Roman')
        with Measure(number='70', width=269.68):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.23, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=83.22, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('tim', font_family='Times New Roman')
            with Note(default_x=114.03, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
            with Note(default_x=144.84, default_y=-352.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=1.77, default_y=-53.23, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben', font_family='Times New Roman')
            with Note(default_x=175.65, default_y=-362.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.18, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('do,', font_family='Times New Roman')
            with Note(default_x=206.46, default_y=-372.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=237.27, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('va', font_family='Times New Roman')
        with Measure(number='71', width=190.32):
            with Note(default_x=31.22, default_y=-382.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=72.21, default_y=-382.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('va,', font_family='Times New Roman')
            with Note(default_x=111.05, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi', font_family='Times New Roman')
            with Note(default_x=149.89, default_y=-377.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('vail', font_family='Times New Roman')
        with Measure(number='72', width=185.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=77.38, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=12.25, default_y=-40.0):
                    Syllabic('single')
                    Text('vin.', font_family='Times New Roman')
        with Measure(number='73', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='74', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='75', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='76', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='77', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='78', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='79', width=106.53):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='80', width=114.13):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')