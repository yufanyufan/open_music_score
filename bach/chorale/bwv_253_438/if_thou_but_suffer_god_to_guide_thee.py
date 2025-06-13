with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Wer nur den lieben Gott läßt walten')
    with Identification():
        Creator('T. und M.: Georg Neumark 1640 ', type='composer')
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
            Millimeters(6.16)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1928.11)
            PageWidth(1364.02)
            with PageMargins(type='even'):
                LeftMargin(32.4676)
                RightMargin(32.4676)
                TopMargin(32.4676)
                BottomMargin(32.4676)
            with PageMargins(type='odd'):
                LeftMargin(32.4676)
                RightMargin(32.4676)
                TopMargin(32.4676)
                BottomMargin(32.4676)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Wer nur den lieben Gott läßt walten', default_x=682.012, default_y=1895.65, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(aus dem Film "Vaya con Dios" 2002)\n', default_x=682.012, default_y=1830.71, justify='center', valign='top', font_size='14')
        CreditWords('c.f. GL 296 / EG 369 (1., 4. u. 7. Str.)')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('T. und M.: Georg Neumark 1640 ', default_x=1331.56, default_y=1709.18, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Bearbeitung: Tobias Gravenhorst', default_x=32.4676, default_y=1709.18, justify='left', valign='bottom', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Gemeinde\n(Sopran)')
            PartAbbreviation('Gem.\nS.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Arbo\n(Alt)')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tassilo\n(Tenor)')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Benno\n(Baß)')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=275.73):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(113.63)
                        RightMargin(-0.0)
                    TopSystemDistance(256.46)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Sound(tempo=100.0)
            with Note(default_x=109.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-14.2, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Wer')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=164.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=219.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='1', width=262.05):
            with Note(default_x=23.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lie')
                with Lyric(number='2', default_x=6.94, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wun')
            with Note(default_x=96.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
            with Note(default_x=141.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('bar')
            with Note(default_x=214.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('läßt')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='2', width=274.59):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wal')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('hal')
            with Note(default_x=59.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=145.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=187.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hof')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=230.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('fet')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
        with Measure(number='3', width=254.8):
            with Note(default_x=21.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Not')
            with Note(default_x=93.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihn')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=137.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Trau')
            with Note(default_x=208.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('rig')
        with Measure(number='4', width=118.29):
            with Note(default_x=22.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.37, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zeit,')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('keit')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=262.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.35)
                        RightMargin(-0.0)
                    SystemDistance(119.39)
            with Note(default_x=88.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('wer')
            with Note(default_x=146.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=203.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='5', width=289.6):
            with Note(default_x=15.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Al')
            with Note(default_x=99.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ler')
            with Note(default_x=151.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('höch')
            with Note(default_x=235.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
        with Measure(number='6', width=278.05):
            with Note(default_x=25.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.67, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('traut,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=142.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=186.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=231.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
        with Measure(number='7', width=279.49):
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kei')
            with Note(default_x=97.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
            with Note(default_x=147.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sand')
            with Note(default_x=227.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='8', width=122.17):
            with Note(default_x=23.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.52, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('baut.')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X2', implicit='yes', width=258.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.35)
                        RightMargin(0.0)
                    SystemDistance(100.0)
            with Note(default_x=88.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-47.16, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.(4.)Er')
            with Note(default_x=144.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('kennt')
            with Note(default_x=201.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='9', width=294.5):
            with Note(default_x=24.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rech')
            with Note(default_x=107.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=158.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=241.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='10', width=323.43):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stun')
            with Note(default_x=62.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=152.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=209.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß')
            with Note(default_x=265.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.96, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl,')
        with Measure(number='11', width=354.97):
            with Note(default_x=27.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('wann')
            with Note(default_x=135.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
            with Note(default_x=192.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nütz')
            with Note(default_x=299.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='12', width=434.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.35)
                        RightMargin(0.0)
                    SystemDistance(100.0)
            with Note(default_x=88.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.46, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=274.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wenn')
            with Note(default_x=327.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=379.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='13', width=395.8):
            with Note(default_x=19.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
            with Note(default_x=153.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=220.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=327.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='14', width=401.59):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=81.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=208.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=272.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer')
            with Note(default_x=336.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
        with Measure(number='15', width=483.48):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.35)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=100.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kei')
            with Note(default_x=234.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=295.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heu')
            with Note(default_x=420.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('che')
        with Measure(number='16', width=395.11):
            with Note(default_x=18.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.05, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('lei.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=222.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('So')
            with Note(default_x=279.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('kommt')
            with Note(default_x=336.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott,')
        with Measure(number='17', width=353.14):
            with Note(default_x=21.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('eh´s')
            with Note(default_x=131.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('wir´s')
            with Note(default_x=186.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=296.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='18', width=504.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.35)
                        RightMargin(0.0)
                    SystemDistance(100.0)
            with Note(default_x=88.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.4, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('sehn,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=287.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=370.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('läs')
            with Note(default_x=436.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('set')
        with Measure(number='19', width=525.59):
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=162.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
            with Note(default_x=252.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gut´s')
            with Note(default_x=433.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='20', width=201.77):
            with Note(default_x=34.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('schehn.')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X3', implicit='yes', width=314.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.03)
                        RightMargin(0.0)
                    SystemDistance(100.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=290.23):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='22', width=288.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='23', width=261.7):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='24', width=106.4):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X4', implicit='yes', width=246.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(38.03)
                        RightMargin(0.0)
                    SystemDistance(120.59)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=285.09):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='26', width=289.88):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='27', width=254.29):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='28', width=184.89):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=275.73):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=262.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=274.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=254.8):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='4', width=118.29):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=262.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=289.6):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='6', width=278.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='7', width=279.49):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='8', width=122.17):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X2', implicit='yes', width=258.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.54)
            with Note(default_x=88.78, default_y=-164.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-47.16, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.(4.)Er')
            with Note(default_x=144.93, default_y=-149.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('kennt')
            with Note(default_x=201.08, default_y=-144.54):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='9', width=294.5):
            with Note(default_x=24.07, default_y=-139.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rech')
            with Note(default_x=107.04, default_y=-144.54):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=158.31, default_y=-149.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=241.27, default_y=-144.54):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='10', width=323.43):
            with Note(default_x=17.23, default_y=-154.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stun')
            with Note(default_x=62.36, default_y=-164.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=152.61, default_y=-154.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=209.02, default_y=-154.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß')
            with Note(default_x=265.43, default_y=-159.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.96, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl,')
        with Measure(number='11', width=354.97):
            with Note(default_x=27.96, default_y=-164.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('wann')
            with Note(default_x=135.65, default_y=-149.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
            with Note(default_x=192.02, default_y=-149.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nütz')
            with Note(default_x=299.71, default_y=-154.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='12', width=434.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.79)
            with Note(default_x=88.78, default_y=-143.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.46, default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=273.8, default_y=-123.79):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nur')
                    Extend()
        with Measure(number='13', width=395.8):
            with Note(default_x=20.08, default_y=-123.79):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.48, default_y=-128.79):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=86.88, default_y=-133.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.29, default_y=-138.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.69, default_y=-143.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=187.1, default_y=-148.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=220.5, default_y=-143.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.12, default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu,')
            with Note(default_x=273.94, default_y=-123.79):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=360.79, default_y=-128.79):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='14', width=401.59):
            with Note(default_x=17.23, default_y=-133.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.08, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=49.13, default_y=-138.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=81.02, default_y=-133.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note(default_x=112.92, default_y=-128.79):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=144.82, default_y=-133.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=176.71, default_y=-128.79):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=208.25, default_y=-138.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer')
            with Note(default_x=336.19, default_y=-143.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
        with Measure(number='15', width=483.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.43)
            with Note(default_x=100.82, default_y=-145.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kei')
            with Note(default_x=131.76, default_y=-120.43):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=162.7, default_y=-120.43):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heu')
            with Note(default_x=234.35, default_y=-120.43):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.32, relative_y=-30.0):
                    Syllabic('middle')
                    Text('che')
            with Note(default_x=295.87, default_y=-120.43):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('lei.')
                    Extend()
        with Measure(number='16', width=395.11):
            with Note(default_x=18.57, default_y=-120.43):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=353.14):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=504.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.21)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=287.69, default_y=-125.21):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=370.41, default_y=-130.21):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('läs')
            with Note(default_x=436.6, default_y=-135.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('set')
        with Measure(number='19', width=525.59):
            with Note(default_x=16.87, default_y=-140.21):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=162.02, default_y=-140.21):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
            with Note(default_x=207.27, default_y=-135.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=252.51, default_y=-130.21):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gut´s')
            with Note(default_x=343.01, default_y=-135.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=433.5, default_y=-140.21):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='20', width=201.77):
            with Note(default_x=34.71, default_y=-145.21):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-45.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('schehn.')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X3', implicit='yes', width=314.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=145.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-46.7, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.(7.)Sing´,')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=204.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.36, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('bet´')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('trau')
            with Note(default_x=254.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='21', width=290.23):
            with Note(default_x=24.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.56, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('geh´')
                with Lyric(number='2', default_x=6.94, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=122.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
            with Note(default_x=174.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Got')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rei')
            with Note(default_x=248.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('tes')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
        with Measure(number='22', width=288.59):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Se')
            with Note(default_x=60.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.61, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
                with Lyric(number='2', default_x=8.61, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=157.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=200.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('richt')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=243.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=261.7):
            with Note(default_x=20.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Dei')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=95.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dir')
            with Note(default_x=131.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
                with Lyric(number='2', default_x=6.22, default_y=-73.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer')
            with Note(default_x=214.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='2', default_x=6.58, default_y=-73.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='24', width=106.4):
            with Note(default_x=22.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('treu')
                with Lyric(number='2', default_x=8.68, default_y=-73.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('neu;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X4', implicit='yes', width=246.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=88.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.58, default_y=-47.02, relative_x=-2.0, relative_y=-40.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=136.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wel')
            with Note(default_x=197.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('cher')
        with Measure(number='25', width=285.09):
            with Note(default_x=16.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
            with Note(default_x=122.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=162.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Zu')
            with Note(default_x=243.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
        with Measure(number='26', width=289.88):
            with Note(default_x=25.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('sicht')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=157.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
            with Note(default_x=200.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=244.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('setzt')
        with Measure(number='27', width=254.29):
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=91.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=128.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('läßt')
            with Note(default_x=202.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='28', width=184.89):
            with Note(default_x=26.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.15, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=275.73):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=262.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=274.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=254.8):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='4', width=118.29):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=262.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=289.6):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='6', width=278.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='7', width=279.49):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='8', width=122.17):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X2', implicit='yes', width=258.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.54)
            with Note(default_x=88.78, default_y=-284.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-47.16, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.(4.)Er')
            with Note(default_x=144.93, default_y=-269.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('kennt')
            with Note(default_x=201.08, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='9', width=294.5):
            with Note(default_x=24.07, default_y=-259.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rech')
            with Note(default_x=107.04, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=158.31, default_y=-269.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=241.27, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
        with Measure(number='10', width=323.43):
            with Note(default_x=17.23, default_y=-274.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stun')
            with Note(default_x=62.36, default_y=-284.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-50.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=152.61, default_y=-274.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=180.81, default_y=-269.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=209.02, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß')
            with Note(default_x=237.22, default_y=-259.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=265.43, default_y=-254.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.96, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl,')
            with Note(default_x=293.63, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=354.97):
            with Note(default_x=28.32, default_y=-249.08):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wann')
            with Note(default_x=55.16, default_y=-254.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=81.99, default_y=-259.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.82, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.65, default_y=-269.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
            with Note(default_x=165.55, default_y=-274.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=192.38, default_y=-269.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nütz')
            with Note(default_x=219.21, default_y=-259.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=246.05, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=272.88, default_y=-254.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=299.71, default_y=-259.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=326.54, default_y=-264.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='12', width=434.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.23)
            with Note(default_x=89.14, default_y=-245.02):
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
                with Lyric(number='1', default_x=0.46, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei.')
                    Extend()
            with Note(default_x=122.18, default_y=-240.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.22, default_y=-245.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.26, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=221.3, default_y=-255.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=274.16, default_y=-270.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wenn')
            with Note(default_x=327.03, default_y=-255.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=379.89, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='13', width=395.8):
            with Note(default_x=19.72, default_y=-245.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
            with Note(default_x=153.69, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=220.14, default_y=-255.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('treu')
            with Note(default_x=327.39, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='14', width=401.59):
            with Note(default_x=17.23, default_y=-260.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
            with Note(default_x=81.02, default_y=-270.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=208.61, default_y=-260.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=240.5, default_y=-255.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=272.4, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-53.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer')
            with Note(default_x=304.3, default_y=-245.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=336.19, default_y=-240.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
            with Note(default_x=368.09, default_y=-250.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=483.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.74)
            with Note(default_x=100.82, default_y=-228.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kei')
            with Note(default_x=131.76, default_y=-233.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=162.7, default_y=-238.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heu')
            with Note(default_x=202.19, default_y=-243.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('middle')
                    Text('che')
            with Note(default_x=234.35, default_y=-248.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.64, default_y=-50.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('lei,')
            with Note(default_x=265.29, default_y=-253.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=296.23, default_y=-248.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=327.17, default_y=-238.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=358.12, default_y=-243.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-50.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer')
            with Note(default_x=389.06, default_y=-233.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=420.0, default_y=-238.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
            with Note(default_x=450.94, default_y=-243.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=395.11):
            with Note(default_x=18.93, default_y=-238.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kei')
            with Note(default_x=54.58, default_y=-233.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=90.23, default_y=-238.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heu')
            with Note(default_x=129.72, default_y=-243.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.77, relative_y=-30.0):
                    Syllabic('middle')
                    Text('che')
            with Note(default_x=165.36, default_y=-248.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-50.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('lei.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=353.14):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=504.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.06)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=436.6, default_y=-243.27):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='19', width=525.59):
            with Note(default_x=17.23, default_y=-248.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('läs')
            with Note(default_x=89.63, default_y=-253.27):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('set')
            with Note(default_x=162.02, default_y=-248.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
            with Note(default_x=207.27, default_y=-243.27):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=252.51, default_y=-238.27):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gut´s')
            with Note(default_x=297.76, default_y=-228.27):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=343.01, default_y=-233.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=388.25, default_y=-228.27):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=433.5, default_y=-243.27):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=478.75, default_y=-268.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='20', width=201.77):
            with Note(default_x=34.71, default_y=-263.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-45.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('schehn.')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X3', implicit='yes', width=314.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.01)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=145.48, default_y=-157.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=-46.7, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.(7.)Sing´,')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=204.44, default_y=-152.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.36, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('bet´')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('trau')
            with Note(default_x=279.69, default_y=-142.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='21', width=290.23):
            with Note(default_x=24.66, default_y=-147.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('geh´')
                    Extend()
                with Lyric(number='2', default_y=-74.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('Him')
                    Extend()
            with Note(default_x=47.62, default_y=-152.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=70.59, default_y=-157.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=93.55, default_y=-162.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.33, default_y=-167.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('mels')
            with Note(default_x=152.23, default_y=-172.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=174.83, default_y=-167.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Got')
                with Lyric(number='2', default_x=6.22, default_y=-74.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rei')
            with Note(default_x=248.68, default_y=-177.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('tes')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
        with Measure(number='22', width=288.59):
            with Note(default_x=16.87, default_y=-162.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
                with Lyric(number='2', default_x=6.22, default_y=-74.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Se')
            with Note(default_x=114.35, default_y=-157.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.61, default_y=-48.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
                with Lyric(number='2', default_x=8.61, default_y=-74.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note(default_x=157.51, default_y=-152.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=200.67, default_y=-147.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('richt')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=243.83, default_y=-152.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=261.7):
            with Note(default_x=21.22, default_y=-167.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Dei')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=58.42, default_y=-172.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
                with Lyric(number='2', default_x=6.58, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dir')
            with Note(default_x=94.68, default_y=-142.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-48.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
                with Lyric(number='2', default_x=6.94, default_y=-74.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer')
            with Note(default_x=168.28, default_y=-147.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='2', default_y=-74.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                    Extend()
            with Note(default_x=191.16, default_y=-152.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=214.05, default_y=-157.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=236.94, default_y=-162.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=106.4):
            with Note(default_x=22.47, default_y=-157.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-48.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('treu')
                with Lyric(number='2', default_x=9.4, default_y=-74.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('neu;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X4', implicit='yes', width=246.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.77)
            with Note(default_x=88.78, default_y=-118.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=136.94, default_y=-118.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wel')
            with Note(default_x=167.04, default_y=-123.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=197.14, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('cher')
                    Extend()
        with Measure(number='25', width=285.09):
            with Note(default_x=17.1, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.26, default_y=-133.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
                    Extend()
            with Note(default_x=67.42, default_y=-138.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=92.58, default_y=-143.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=122.47, default_y=-148.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Note(default_x=162.73, default_y=-143.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Zu')
            with Note(default_x=202.98, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.24, default_y=-123.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
        with Measure(number='26', width=289.88):
            with Note(default_x=25.8, default_y=-118.77):
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
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('sicht')
                    Extend()
            with Note(default_x=69.55, default_y=-123.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.94, default_y=-108.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
            with Note(default_x=200.79, default_y=-113.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=244.54, default_y=-118.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('setzt')
        with Measure(number='27', width=254.29):
            with Note(default_x=17.23, default_y=-123.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=54.3, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.37, default_y=-133.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=128.44, default_y=-118.77):
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
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('läßt')
            with Note(default_x=165.51, default_y=-123.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.74, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                    Extend()
        with Measure(number='28', width=184.89):
            with Note(default_x=27.31, default_y=-128.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.88, default_y=-133.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=99.74, default_y=-138.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=130.72, default_y=-133.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.51, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='0', implicit='yes', width=275.73):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('6')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=262.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=274.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=254.8):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='4', width=118.29):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=262.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=289.6):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='6', width=278.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='7', width=279.49):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='8', width=122.17):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X2', implicit='yes', width=258.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.51)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(6.0)
            with Note(default_x=88.78, default_y=-388.6, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
        with Measure(number='9', width=294.5):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='10', width=323.43):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='11', width=354.97):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='12', width=434.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.94)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
            with Backup():
                Duration(12.0)
            with Note(default_x=89.14, default_y=-367.96, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('2')
                Type('whole')
        with Measure(number='13', width=395.8):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='14', width=401.59):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='15', width=483.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.38)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=358.12, default_y=-337.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heu')
            with Note(default_x=420.0, default_y=-347.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('middle')
                    Text('che')
        with Measure(number='16', width=395.11):
            with Note(default_x=18.57, default_y=-367.54):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('lei.')
                    Extend()
            with Note(default_x=165.36, default_y=-332.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=353.14):
            with Note(default_x=21.91, default_y=-312.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('So')
            with Note(default_x=76.82, default_y=-322.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-49.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('kommt,')
            with Note(default_x=131.89, default_y=-332.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('eh´s')
            with Note(default_x=186.8, default_y=-342.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('wir´s')
            with Note(default_x=241.71, default_y=-352.54):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=296.63, default_y=-362.54):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='18', width=504.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.09)
            with Note(default_x=89.14, default_y=-379.36):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('sehn')
                    Extend()
            with Note(default_x=155.32, default_y=-374.36):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=221.5, default_y=-369.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=287.69, default_y=-364.36):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=329.05, default_y=-359.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=370.41, default_y=-359.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('läs')
            with Note(default_x=436.6, default_y=-354.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('set')
        with Measure(number='19', width=525.59):
            with Note(default_x=16.87, default_y=-349.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=162.02, default_y=-354.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
            with Note(default_x=252.15, default_y=-339.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gut´s')
            with Note(default_x=433.5, default_y=-349.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='20', width=201.77):
            with Note(default_x=34.71, default_y=-344.36):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('schehn.')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='X3', implicit='yes', width=314.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(101.87)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=145.48, default_y=-283.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=-46.7, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.(7.)Sing´,')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=174.96, default_y=-288.87):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=204.44, default_y=-293.87):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=9.36, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('bet´')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('trau')
            with Note(default_x=229.52, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=254.61, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='21', width=290.23):
            with Note(default_x=24.66, default_y=-308.87):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('geh´')
                    Extend()
                with Lyric(number='2', default_y=-74.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=70.59, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.33, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
            with Note(default_x=175.2, default_y=-293.87):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Got')
                with Lyric(number='2', default_y=-74.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rei')
            with Note(default_x=211.94, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=248.68, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('tes')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('chem')
        with Measure(number='22', width=288.59):
            with Note(default_x=17.23, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-48.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
                with Lyric(number='2', default_y=-74.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Se')
            with Note(default_x=87.37, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.35, default_y=-308.87):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.61, default_y=-48.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
                with Lyric(number='2', default_x=8.61, default_y=-74.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen,')
            with Note(default_x=157.51, default_y=-313.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=200.67, default_y=-308.87):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('richt')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=243.83, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='23', width=261.7):
            with Note(default_x=20.86, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-48.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Dei')
                with Lyric(number='2', default_x=6.94, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=95.04, default_y=-293.87):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dir')
            with Note(default_x=131.66, default_y=-303.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
                with Lyric(number='2', default_y=-74.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer')
            with Note(default_x=168.28, default_y=-313.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.05, default_y=-298.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='2', default_x=6.58, default_y=-74.6, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='24', width=106.4):
            with Note(default_x=22.47, default_y=-318.87):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('treu')
                with Lyric(number='2', default_x=8.68, default_y=-74.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('neu;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X4', implicit='yes', width=246.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.17)
            with Note(default_x=88.78, default_y=-248.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
            with Note(default_x=136.94, default_y=-253.94):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wel')
            with Note(default_x=197.14, default_y=-258.94):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('cher')
        with Measure(number='25', width=285.09):
            with Note(default_x=17.1, default_y=-253.94):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
            with Note(default_x=67.42, default_y=-248.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.47, default_y=-243.94):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=162.73, default_y=-238.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Zu')
            with Note(default_x=202.98, default_y=-238.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.24, default_y=-233.94):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
        with Measure(number='26', width=289.88):
            with Note(default_x=25.44, default_y=-228.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('sicht')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=157.04, default_y=-238.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
            with Note(default_x=200.79, default_y=-233.94):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=244.54, default_y=-248.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('setzt')
        with Measure(number='27', width=254.29):
            with Note(default_x=16.87, default_y=-243.94):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=91.37, default_y=-238.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=128.44, default_y=-248.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('läßt')
            with Note(default_x=165.15, default_y=-243.94):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='28', width=184.89):
            with Note(default_x=26.95, default_y=-228.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht.')
            with Barline(location='right'):
                BarStyle('light-heavy')