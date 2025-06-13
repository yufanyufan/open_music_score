with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Himno de la Alegría 3 ')
    with Identification():
        Creator('Miguel Ríos', type='composer')
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
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.36)
            PageWidth(1190.88)
            with PageMargins(type='even'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
            with PageMargins(type='odd'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Himno de la Alegría  ', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Miguel Ríos', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Guitarra clásica')
            PartAbbreviation('Guit.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Guitarra clásica')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(25)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=116.41):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
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
        with Measure(number='2', width=62.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=132.51):
            with Note(default_x=15.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Es')
            with Note(default_x=67.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cu')
            with Note(default_x=98.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cha')
        with Measure(number='4', width=198.31):
            with Note(default_x=35.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her͜\xa0ma')
            with Note(default_x=82.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('no')
            with Note(default_x=120.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=158.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
        with Measure(number='5', width=159.87):
            with Note(default_x=23.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ción')
            with Note(default_x=57.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=91.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=124.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ale')
        with Measure(number='6', width=108.18):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('grí')
                    Extend()
            with Note(default_x=44.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=69.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
        with Measure(number='7', width=121.67):
            with Note(default_x=14.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='2', default_x=6.94, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('El')
            with Note(default_x=61.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=91.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('to')
        with Measure(number='8', width=178.39):
            with Note(default_x=17.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ale')
            with Note(default_x=57.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('gre')
            with Note(default_x=97.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=137.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('te͜\xa0es')
        with Measure(number='9', width=231.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(96.56)
            with Note(default_x=56.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe')
            with Note(default_x=99.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra͜\xa0un')
            with Note(default_x=143.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nue')
            with Note(default_x=186.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('vo')
        with Measure(number='10', width=107.72):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='2', default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('dí')
                    Extend()
            with Note(default_x=44.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=69.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='2', default_x=6.22, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
        with Measure(number='11', width=161.44):
            with Note(default_x=15.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.11, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve͜')
            with Note(default_x=51.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('en')
            with Note(default_x=87.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=123.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ta')
        with Measure(number='12', width=203.12):
            with Note(default_x=19.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('sue')
            with Note(default_x=59.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('ña')
            with Note(default_x=86.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=121.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tan')
            with Note(default_x=161.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do')
        with Measure(number='13', width=211.04):
            with Note(default_x=13.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=58.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=87.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=118.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ñan')
            with Note(default_x=163.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do\xa0͜el')
        with Measure(number='14', width=162.62):
            with Note(default_x=21.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nue')
            with Note(default_x=55.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('vo')
            with Note(default_x=89.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('sol')
            with Note(default_x=131.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
        with Measure(number='15', width=172.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(94.76)
            with Note(default_x=56.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=139.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('los')
        with Measure(number='16', width=216.15):
            with Note(default_x=24.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hom')
            with Note(default_x=72.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('bres')
            with Note(default_x=119.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vol')
            with Note(default_x=167.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
        with Measure(number='17', width=160.59):
            with Note(default_x=19.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('rán')
            with Note(default_x=54.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=89.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
            with Note(default_x=124.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
        with Measure(number='18', width=147.41):
            with Note(default_x=26.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ma͜\xa0a')
            with Note(default_x=70.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('nos')
            with Note(default_x=95.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=169.43):
            with Note(default_x=15.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.11, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve͜')
            with Note(default_x=53.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('en')
            with Note(default_x=91.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=129.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ta')
        with Measure(number='20', width=211.11):
            with Note(default_x=19.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sue')
            with Note(default_x=62.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ña')
            with Note(default_x=89.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=124.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tan')
            with Note(default_x=166.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('do')
        with Measure(number='21', width=251.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(94.76)
            with Note(default_x=56.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=101.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=129.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=160.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ñan')
            with Note(default_x=204.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('do\xa0͜el')
        with Measure(number='22', width=159.51):
            with Note(default_x=21.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nue')
            with Note(default_x=54.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('vo')
            with Note(default_x=87.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sol')
            with Note(default_x=127.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
        with Measure(number='23', width=117.45):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=87.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('los')
        with Measure(number='24', width=205.05):
            with Note(default_x=24.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hom')
            with Note(default_x=69.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('bres')
            with Note(default_x=114.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vol')
            with Note(default_x=158.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
        with Measure(number='25', width=149.49):
            with Note(default_x=19.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('rán')
            with Note(default_x=50.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=82.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
            with Note(default_x=113.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
        with Measure(number='26', width=136.31):
            with Note(default_x=26.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ma͜\xa0a')
            with Note(default_x=65.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('nos')
            with Note(default_x=90.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='27', width=58.57):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=91.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(94.76)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='39', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='40', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='43', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=58.02):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='46', width=97.73):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(94.76)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='47', width=64.53):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='48', width=64.53):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='49', width=137.97):
            with Note(default_x=26.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Si͜\xa0en')
            with Note(default_x=75.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
            with Note(default_x=105.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ca')
        with Measure(number='50', width=146.37):
            with Note(default_x=16.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=48.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('no')
            with Note(default_x=80.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('só')
            with Note(default_x=112.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lo')
        with Measure(number='51', width=133.87):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=42.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('xis')
            with Note(default_x=72.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
            with Note(default_x=102.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
        with Measure(number='52', width=121.74):
            with Note(default_x=19.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tris')
            with Note(default_x=54.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Note(default_x=79.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('za')
        with Measure(number='53', width=145.37):
            with Note(default_x=23.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='2', default_x=6.94, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Y͜\xa0el')
            with Note(default_x=77.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('llan')
            with Note(default_x=110.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('to')
        with Measure(number='54', width=165.41):
            with Note(default_x=27.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('amar')
            with Note(default_x=65.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('go')
            with Note(default_x=98.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=131.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
        with Measure(number='55', width=219.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(100.96)
            with Note(default_x=56.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=96.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=137.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('dad')
            with Note(default_x=177.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('com')
        with Measure(number='56', width=113.68):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='2', default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ple')
                    Extend()
            with Note(default_x=47.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=72.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='2', default_x=8.32, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('ta.')
        with Measure(number='57', width=162.58):
            with Note(default_x=18.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.15, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ve͜')
            with Note(default_x=53.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
            with Note(default_x=89.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=125.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ta')
        with Measure(number='58', width=208.13):
            with Note(default_x=19.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sue')
            with Note(default_x=61.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ña')
            with Note(default_x=88.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=123.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tan')
            with Note(default_x=164.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do')
        with Measure(number='59', width=211.25):
            with Note(default_x=13.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=58.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=87.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=118.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ñan')
            with Note(default_x=164.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do͜\xa0el')
        with Measure(number='60', width=162.83):
            with Note(default_x=21.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nue')
            with Note(default_x=55.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('vo')
            with Note(default_x=89.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('sol')
            with Note(default_x=131.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
        with Measure(number='61', width=147.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(94.76)
            with Note(default_x=56.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('qe')
            with Note(default_x=117.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('los')
        with Measure(number='62', width=195.13):
            with Note(default_x=24.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hom')
            with Note(default_x=68.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('bres')
            with Note(default_x=110.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vol')
            with Note(default_x=151.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ve')
        with Measure(number='63', width=148.69):
            with Note(default_x=19.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('rán')
            with Note(default_x=50.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=81.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
            with Note(default_x=112.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
        with Measure(number='64', width=123.58):
            with Note(default_x=18.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma')
            with Note(default_x=55.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('nos')
            with Note(default_x=80.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='65', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='66', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='67', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='68', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='69', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='70', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='71', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='72', width=57.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='73', width=92.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(94.76)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='74', width=59.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='75', width=59.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='76', width=59.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='77', width=59.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='78', width=175.45):
            with Note(default_x=25.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Si͜\xa0es')
            with Note(default_x=91.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=132.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('no\xa0en')
        with Measure(number='79', width=174.57):
            with Note(default_x=25.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('cuen')
            with Note(default_x=63.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('tras')
            with Note(default_x=100.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=136.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ale')
        with Measure(number='80', width=157.53):
            with Note(default_x=17.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('grí')
            with Note(default_x=53.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('a\xa0en')
            with Note(default_x=87.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('es')
            with Note(default_x=121.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ta')
        with Measure(number='81', width=116.02):
            with Note(default_x=16.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tie')
            with Note(default_x=50.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Note(default_x=75.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('rra')
        with Measure(number='82', width=123.41):
            with Note(default_x=21.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='2', default_x=6.94, default_y=-73.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bus')
            with Note(default_x=66.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ca')
            with Note(default_x=93.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-73.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
        with Measure(number='83', width=218.52):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(94.76)
            with Note(default_x=56.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
            with Note(default_x=96.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma')
            with Note(default_x=136.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('no')
            with Note(default_x=176.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('más')
        with Measure(number='84', width=146.58):
            with Note(default_x=20.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('alla')
            with Note(default_x=51.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=82.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('las')
            with Note(default_x=113.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
        with Measure(number='85', width=125.97):
            with Note(default_x=17.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=55.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='2', default_x=6.58, default_y=-72.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Note(default_x=80.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='2', default_x=8.13, default_y=-72.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('llas.')
        with Measure(number='86', width=161.83):
            with Note(default_x=18.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.15, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ve͜')
            with Note(default_x=53.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
            with Note(default_x=89.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=124.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ta')
        with Measure(number='87', width=207.38):
            with Note(default_x=19.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sue')
            with Note(default_x=60.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ña')
            with Note(default_x=88.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can')
            with Note(default_x=123.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tan')
            with Note(default_x=164.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do')
        with Measure(number='88', width=217.22):
            with Note(default_x=13.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=60.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=90.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=121.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ñan')
            with Note(default_x=168.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.43, default_y=-46.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('do͜\xa0el\xa0\xa0')
        with Measure(number='89', width=195.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=56.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nue')
            with Note(default_x=89.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('vo')
            with Note(default_x=122.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sol')
            with Note(default_x=163.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
        with Measure(number='90', width=117.43):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=87.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('los')
        with Measure(number='91', width=195.9):
            with Note(default_x=24.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hom')
            with Note(default_x=68.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('bres')
            with Note(default_x=110.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vol')
            with Note(default_x=152.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ve')
        with Measure(number='92', width=149.46):
            with Note(default_x=19.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('rán')
            with Note(default_x=50.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=81.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
            with Note(default_x=113.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
        with Measure(number='93', width=126.9):
            with Note(default_x=18.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma')
            with Note(default_x=56.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('a')
            with Note(default_x=82.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.21, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('nos.')
        with Measure(number='94', width=58.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='95', width=58.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='96', width=58.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='97', width=58.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='98', width=58.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='99', width=113.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='100', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='101', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='102', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='103', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='104', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='105', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='106', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='107', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='108', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='109', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='110', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='111', width=80.33):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')