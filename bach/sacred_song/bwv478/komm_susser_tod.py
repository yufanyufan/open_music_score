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
            Millimeters(5.632)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1984.37)
            PageWidth(1533.38)
            with PageMargins(type='both'):
                LeftMargin(71.0227)
                RightMargin(71.0227)
                TopMargin(71.0227)
                BottomMargin(106.534)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Komm, süßer Tod', default_x=766.69, default_y=1917.22, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J.S. Bach (BWV 478)', default_x=1462.36, default_y=1855.38, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(84.252)
                Pan(-26.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(83.4646)
                Pan(36.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(81.8898)
                Pan(-58.0)
        with ScorePart(id='P4'):
            PartName('Basse')
            PartAbbreviation('B')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(82.6772)
                Pan(61.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=289.72):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(94.18)
                        RightMargin(-0.0)
                    TopSystemDistance(184.39)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Sound(tempo=80.0)
            with Note(default_x=118.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=-18.33, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text(" 1.2.3.Komm'", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=188.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sü')
            with Note(default_x=232.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer')
                    Extend()
            with Note(default_x=260.55, default_y=-30.0):
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
        with Measure(number='2', width=79.67):
            with Note(default_x=22.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,', font_family='Times New Roman', font_size='10.7316')
        with Measure(number='3', width=197.45):
            with Note(default_x=32.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.87, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=84.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.4, default_y=-46.93, relative_y=-30.0):
                    Syllabic('middle')
                    Text("sel'", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=134.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
            with Note(default_x=164.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=78.39):
            with Note(default_x=14.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=12.04, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("Ruh'!", font_family='Times New Roman', font_size='10.7316')
        with Measure(number='5', width=230.43):
            with Note(default_x=34.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
            with Note(default_x=92.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
            with Note(default_x=171.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
        with Measure(number='6', width=140.52):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('mich', font_family='Times New Roman', font_size='10.7316')
                    Extend()
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                    Extend()
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=51.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.46, default_y=-35.0):
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
            with Note(default_x=99.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('sum')
        with Measure(number='7', width=130.58):
            with Note(default_x=21.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.22, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bes')
                with Lyric(number='3', default_x=6.22, default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=95.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
                with Lyric(number='2', default_x=9.13, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser,')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('hen')
        with Measure(number='8', width=150.4):
            with Note(default_x=23.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=65.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=107.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
        with Measure(number='9', width=488.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(39.06)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=97.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('Welt', font_family='Times New Roman', font_size='10.7316')
                    Extend()
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust')
                    Extend()
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=208.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=347.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('geln')
            with Note(default_x=417.09, default_y=-15.0):
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
        with Measure(number='10', width=407.03):
            with Note(default_x=19.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mü')
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('grö')
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ste')
            with Note(default_x=138.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=286.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('de,')
                with Lyric(number='2', default_x=9.01, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ßer,')
                with Lyric(number='3', default_x=8.85, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen.')
        with Measure(number='11', width=457.05):
            with Note(default_x=28.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=150.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=11.17, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=302.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nun')
            with Note(default_x=379.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=347.48):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(39.06)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=97.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.14, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text("wart'")
                with Lyric(number='2', default_x=12.89, default_y=-70.88, relative_x=6.3, relative_y=-77.56):
                    Syllabic('begin')
                    Text('je')
                with Lyric(number='3', default_x=6.58, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
            with Note(default_x=185.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                    Extend()
                with Lyric(number='2', default_y=-70.88, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
                with Lyric(number='3', default_y=-94.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
            with Note(default_x=290.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=318.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=265.53):
            with Note(default_x=32.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.83, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich,')
                with Lyric(number='2', default_x=6.22, default_y=-70.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('zeit')
                with Lyric(number='3', default_x=8.44, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('bracht,')
        with Measure(number='14', width=293.05):
            with Note(default_x=35.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.26, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text("Komm'")
                with Lyric(number='2', default_x=6.58, default_y=-70.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
                with Lyric(number='3', default_x=9.1, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum,')
            with Note(default_x=78.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=121.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('bald')
                with Lyric(number='2', default_x=6.58, default_y=-70.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('zum')
                with Lyric(number='3', default_x=8.85, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt,')
            with Note(default_x=206.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-70.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='3', default_x=6.58, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='15', width=228.13):
            with Note(default_x=20.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.43, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
                with Lyric(number='2', default_x=6.58, default_y=-70.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('let')
                with Lyric(number='3', default_x=6.58, default_y=-94.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=83.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.43, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                    Extend()
                with Lyric(number='2', default_y=-70.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='3', default_y=-94.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
                    Extend()
            with Note(default_x=123.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=163.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=218.1):
            with Note(default_x=31.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-47.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich,')
                with Lyric(number='2', default_x=9.11, default_y=-70.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('reit,')
                with Lyric(number='3', default_x=9.23, default_y=-94.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
        with Measure(number='17', width=377.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(39.06)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=97.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.9, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("drück'")
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=176.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
                    Extend()
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('schließ')
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
            with Note(default_x=226.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=276.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
            with Note(default_x=325.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=271.18):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind')
                    Extend()
            with Note(default_x=54.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=140.79, default_y=-15.0):
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
            with Note(default_x=183.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
            with Note(default_x=226.65, default_y=-15.0):
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
        with Measure(number='19', width=226.85):
            with Note(default_x=13.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.5, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                with Lyric(number='2', default_x=8.5, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                with Lyric(number='3', default_x=8.5, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
        with Measure(number='20', width=277.9):
            with Note(default_x=33.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=11.17, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=11.17, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='3', default_x=11.17, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
            with Note(default_x=74.09, default_y=-30.0):
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
            with Note(default_x=114.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='2', default_x=8.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='3', default_x=8.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=195.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
            with Note(default_x=235.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=199.26):
            with Note(default_x=23.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.75, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='2', default_x=9.75, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='3', default_x=9.75, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward', times=3)
    with Part(id='P2'):
        with Measure(number='1', width=289.72):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(109.72)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(1)
            with Note(default_x=118.43, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-46.98, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("1.2.3.Komm'", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=188.89, default_y=-184.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sü')
            with Note(default_x=232.99, default_y=-194.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer')
        with Measure(number='2', width=79.67):
            with Note(default_x=22.41, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,', font_family='Times New Roman', font_size='10.7316')
        with Measure(number='3', width=197.45):
            with Note(default_x=32.95, default_y=-179.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.87, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=84.52, default_y=-184.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=134.0, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='4', width=78.39):
            with Note(default_x=14.36, default_y=-194.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=11.28, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("Ruh'!")
        with Measure(number='5', width=230.43):
            with Note(default_x=34.84, default_y=-179.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
            with Note(default_x=127.99, default_y=-184.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
            with Note(default_x=171.81, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
        with Measure(number='6', width=140.52):
            with Note(default_x=12.0, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-65.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('mich', font_family='Times New Roman', font_size='10.7316')
                    Extend()
                with Lyric(number='2', default_y=-89.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                    Extend()
                with Lyric(number='3', default_y=-112.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=51.05, default_y=-204.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.87, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('sum')
        with Measure(number='7', width=130.58):
            with Note(default_x=22.2, default_y=-189.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-65.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
                with Lyric(number='2', default_y=-89.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bes')
                with Lyric(number='3', default_y=-112.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=54.59, default_y=-194.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.07, default_y=-204.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen')
        with Measure(number='8', width=150.4):
            with Note(default_x=23.96, default_y=-179.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=65.57, default_y=-184.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=107.18, default_y=-184.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-89.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='3', default_x=6.58, default_y=-112.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
        with Measure(number='9', width=488.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(113.73)
            with Note(default_x=97.38, default_y=-193.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
                with Lyric(number='2', default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust')
                    Extend()
                with Lyric(number='3', default_y=-117.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=208.58, default_y=-198.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=347.59, default_y=-198.73):
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
                with Lyric(number='1', default_x=6.58, default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='2', default_x=6.58, default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
                with Lyric(number='3', default_x=6.58, default_y=-117.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('geln')
            with Note(default_x=417.09, default_y=-193.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=407.03):
            with Note(default_x=19.7, default_y=-198.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-70.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mü')
                with Lyric(number='2', default_y=-93.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('grö')
                with Lyric(number='3', default_y=-117.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ste')
            with Note(default_x=212.56, default_y=-203.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=286.74, default_y=-208.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('de,')
                with Lyric(number='2', default_x=9.01, default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('ßer,')
                with Lyric(number='3', default_x=8.85, default_y=-117.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen.')
        with Measure(number='11', width=457.05):
            with Note(default_x=28.47, default_y=-183.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach')
                with Lyric(number='2', default_x=6.58, default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum')
                with Lyric(number='3', default_x=6.58, default_y=-117.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=150.46, default_y=-178.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.17, default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=6.58, default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='3', default_x=6.58, default_y=-117.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=302.96, default_y=-183.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-70.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-93.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-117.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nun')
        with Measure(number='12', width=347.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(138.35)
            with Note(default_x=97.38, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.14, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("wart'")
                with Lyric(number='2', default_x=6.58, default_y=-82.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
                with Lyric(number='3', default_x=6.58, default_y=-105.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=185.73, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                    Extend()
                with Lyric(number='2', default_y=-82.13, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
                with Lyric(number='3', default_y=-105.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
            with Note(default_x=246.48, default_y=-218.35):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=265.53):
            with Note(default_x=32.66, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.83, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich,')
                with Lyric(number='2', default_x=6.22, default_y=-82.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('zeit')
                with Lyric(number='3', default_x=8.44, default_y=-105.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('bracht,')
            with Note(default_x=181.46, default_y=-193.35):
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
                with Lyric(number='1', default_x=8.26, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("Komm'")
                with Lyric(number='2', default_x=6.58, default_y=-82.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
                with Lyric(number='3', default_x=9.1, default_y=-105.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum,')
            with Note(default_x=222.69, default_y=-203.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=293.05):
            with Note(default_x=35.81, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('bald')
                    Extend()
                with Lyric(number='2', default_y=-82.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('zum')
                    Extend()
                with Lyric(number='3', default_y=-105.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt,')
                    Extend()
            with Note(default_x=163.63, default_y=-218.35):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.23, default_y=-213.35):
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
                with Lyric(number='1', default_x=6.58, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_y=-82.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='3', default_x=6.58, default_y=-105.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=248.84, default_y=-223.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=228.13):
            with Note(default_x=20.45, default_y=-218.35):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
                with Lyric(number='2', default_y=-82.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('let')
                    Extend()
                with Lyric(number='3', default_y=-105.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=83.86, default_y=-208.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=163.12, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-82.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-105.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('ter')
        with Measure(number='16', width=218.1):
            with Note(default_x=31.34, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.5, default_y=-58.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich,')
                with Lyric(number='2', default_x=8.39, default_y=-82.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('reit,')
                with Lyric(number='3', default_x=8.5, default_y=-105.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
        with Measure(number='17', width=377.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(112.37)
            with Note(default_x=97.38, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.9, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text("drück'")
                with Lyric(number='2', default_x=6.58, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=176.84, default_y=-172.37):
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
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
                    Extend()
                with Lyric(number='2', default_x=6.58, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('schließ')
                with Lyric(number='3', default_y=-111.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
            with Note(default_x=226.5, default_y=-177.37):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=276.16, default_y=-182.37):
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
                with Lyric(number='1', default_x=6.58, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-111.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=325.82, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=271.18):
            with Note(default_x=12.0, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='2', default_y=-87.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='3', default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind')
                    Extend()
            with Note(default_x=97.86, default_y=-187.37):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.72, default_y=-177.37):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='3', default_x=6.58, default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
        with Measure(number='19', width=226.85):
            with Note(default_x=14.0, default_y=-197.37):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='2', default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='3', default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
            with Note(default_x=74.0, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=277.9):
            with Note(default_x=33.65, default_y=-202.37):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.17, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=11.17, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='3', default_x=11.17, default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
            with Note(default_x=114.54, default_y=-202.37):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.5, default_y=-64.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='2', default_x=0.5, default_y=-87.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='3', default_x=0.5, default_y=-111.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=154.98, default_y=-182.37):
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
            with Note(default_x=195.42, default_y=-182.37):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='2', default_y=-87.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='3', default_y=-111.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
            with Note(default_x=235.86, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=199.26):
            with Note(default_x=23.3, default_y=-192.37):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.03, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='2', default_x=9.03, default_y=-87.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='3', default_x=9.03, default_y=-111.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward', times=3)
    with Part(id='P3'):
        with Measure(number='1', width=289.72):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(143.72)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Note(default_x=118.43, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-46.98, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("1.2.3.Komm'", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=188.89, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sü')
            with Note(default_x=232.99, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer')
        with Measure(number='2', width=79.67):
            with Note(default_x=22.41, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.38, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,', font_family='Times New Roman', font_size='10.7316')
        with Measure(number='3', width=197.45):
            with Note(default_x=32.95, default_y=-348.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.87, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=84.52, default_y=-358.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=134.0, default_y=-358.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='4', width=78.39):
            with Note(default_x=14.36, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=11.28, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("Ruh'!")
        with Measure(number='5', width=230.43):
            with Note(default_x=34.84, default_y=-348.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.5, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,', font_family='Times New Roman', font_size='10.7316')
                    Extend()
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
                    Extend()
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
                    Extend()
            with Note(default_x=92.35, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.99, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('will')
            with Note(default_x=171.81, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('nun')
        with Measure(number='6', width=140.52):
            with Note(default_x=12.0, default_y=-348.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
                    Extend()
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('ist')
                    Extend()
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=51.05, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.87, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('sum')
        with Measure(number='7', width=130.58):
            with Note(default_x=22.2, default_y=-348.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bes')
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=54.59, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.83, default_y=-358.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.07, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
                with Lyric(number='2', default_x=9.13, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser,')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen')
        with Measure(number='8', width=150.4):
            with Note(default_x=23.96, default_y=-353.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=65.57, default_y=-348.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=107.18, default_y=-363.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
        with Measure(number='9', width=488.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(155.47)
            with Note(default_x=97.38, default_y=-379.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
                with Lyric(number='2', default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust')
                    Extend()
                with Lyric(number='3', default_y=-114.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=208.58, default_y=-374.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=347.59, default_y=-369.2):
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
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='2', default_x=6.58, default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
                with Lyric(number='3', default_x=6.58, default_y=-114.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('geln')
            with Note(default_x=417.09, default_y=-394.2):
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
        with Measure(number='10', width=407.03):
            with Note(default_x=19.7, default_y=-379.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-67.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mü')
                with Lyric(number='2', default_y=-91.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('grö')
                with Lyric(number='3', default_y=-114.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ste')
            with Note(default_x=138.38, default_y=-384.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=286.74, default_y=-379.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de,')
                with Lyric(number='2', default_x=9.01, default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('ßer,')
                with Lyric(number='3', default_x=8.85, default_y=-114.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen.')
        with Measure(number='11', width=457.05):
            with Note(default_x=28.47, default_y=-354.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach')
                with Lyric(number='2', default_x=6.58, default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum')
                with Lyric(number='3', default_x=6.58, default_y=-114.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=150.46, default_y=-369.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=11.17, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=6.58, default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='3', default_x=6.58, default_y=-114.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=226.71, default_y=-374.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.96, default_y=-364.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-91.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-114.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nun')
        with Measure(number='12', width=347.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(142.54)
            with Note(default_x=97.38, default_y=-375.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=8.14, default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("wart'")
                with Lyric(number='2', default_y=-67.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
                with Lyric(number='3', default_x=6.58, default_y=-90.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=141.56, default_y=-385.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=185.73, default_y=-370.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                    Extend()
                with Lyric(number='2', default_y=-67.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der')
                with Lyric(number='3', default_y=-90.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
            with Note(default_x=246.48, default_y=-375.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=265.53):
            with Note(default_x=33.02, default_y=-375.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich,')
                with Lyric(number='2', default_x=8.7, default_y=-67.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('zeit,')
                with Lyric(number='3', default_x=8.8, default_y=-90.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('bracht,')
            with Note(default_x=98.99, default_y=-395.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("Komm'")
                    Extend()
                with Lyric(number='2', default_y=-67.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
                    Extend()
                with Lyric(number='3', default_x=0.5, default_y=-90.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum,')
                    Extend()
            with Note(default_x=140.22, default_y=-390.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=181.46, default_y=-385.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=222.69, default_y=-375.89):
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
        with Measure(number='14', width=293.05):
            with Note(default_x=35.45, default_y=-380.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('bald')
                with Lyric(number='2', default_x=6.22, default_y=-67.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('zum')
                with Lyric(number='3', default_x=8.48, default_y=-90.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt,')
            with Note(default_x=206.23, default_y=-380.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-67.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='3', default_x=6.58, default_y=-90.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='15', width=228.13):
            with Note(default_x=20.45, default_y=-380.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-43.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
                with Lyric(number='2', default_y=-67.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('let')
                    Extend()
                with Lyric(number='3', default_y=-90.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=83.86, default_y=-375.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=163.12, default_y=-385.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-67.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-90.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('ter')
        with Measure(number='16', width=218.1):
            with Note(default_x=31.7, default_y=-380.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich,')
                    Extend()
                with Lyric(number='2', default_y=-67.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('reit,')
                    Extend()
                with Lyric(number='3', default_y=-90.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
                    Extend()
            with Note(default_x=84.5, default_y=-370.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=183.5, default_y=-375.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=377.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(149.35)
            with Note(default_x=97.38, default_y=-381.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.9, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("drück'")
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=176.84, default_y=-346.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('schließ')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
            with Note(default_x=276.16, default_y=-361.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
        with Measure(number='18', width=271.18):
            with Note(default_x=12.0, default_y=-356.72):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind')
                    Extend()
            with Note(default_x=97.86, default_y=-366.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.72, default_y=-351.72):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
            with Note(default_x=226.65, default_y=-356.72):
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
        with Measure(number='19', width=226.85):
            with Note(default_x=14.0, default_y=-361.72):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
            with Note(default_x=74.0, default_y=-356.72):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=277.9):
            with Note(default_x=33.65, default_y=-351.72):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.17, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=11.17, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='3', default_x=11.17, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
            with Note(default_x=114.54, default_y=-346.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='2', default_x=8.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='3', default_x=8.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=195.42, default_y=-361.72):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                    Extend()
            with Note(default_x=235.86, default_y=-356.72):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=199.26):
            with Note(default_x=23.3, default_y=-356.72):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.75, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='2', default_x=9.75, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='3', default_x=9.75, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward', times=3)
    with Part(id='P4'):
        with Measure(number='1', width=289.72):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(124.47)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=118.43, default_y=-522.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-47.56, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.2.3.')
                    Text("Komm'", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=188.89, default_y=-517.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sü')
            with Note(default_x=232.99, default_y=-527.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer')
        with Measure(number='2', width=79.67):
            with Note(default_x=22.41, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.38, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,', font_family='Times New Roman', font_size='10.7316')
        with Measure(number='3', width=197.45):
            with Note(default_x=32.95, default_y=-522.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.87, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',", font_family='Times New Roman', font_size='10.7316')
            with Note(default_x=84.52, default_y=-507.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=134.0, default_y=-507.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='4', width=78.39):
            with Note(default_x=14.36, default_y=-502.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=12.01, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text("Ruh'!")
        with Measure(number='5', width=230.43):
            with Note(default_x=34.84, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
            with Note(default_x=92.35, default_y=-527.91):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Him')
                    Extend()
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
            with Note(default_x=171.81, default_y=-522.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('mel')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
        with Measure(number='6', width=140.52):
            with Note(default_x=12.0, default_y=-522.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
                    Extend()
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                    Extend()
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=51.05, default_y=-517.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.87, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('sum')
        with Measure(number='7', width=130.58):
            with Note(default_x=22.2, default_y=-532.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
                with Lyric(number='2', default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bes')
                with Lyric(number='3', default_y=-93.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=54.59, default_y=-527.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.07, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('hen')
        with Measure(number='8', width=150.4):
            with Note(default_x=23.96, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=65.57, default_y=-512.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('bei')
            with Note(default_x=107.18, default_y=-517.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='10.7316')
                with Lyric(number='2', default_x=6.58, default_y=-70.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='3', default_x=6.58, default_y=-93.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
        with Measure(number='9', width=488.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(143.57)
            with Note(default_x=97.38, default_y=-557.77):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                    Extend()
                with Lyric(number='2', default_y=-74.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust')
                    Extend()
                with Lyric(number='3', default_y=-97.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=208.58, default_y=-542.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=347.59, default_y=-537.77):
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
                with Lyric(number='1', default_x=6.58, default_y=-50.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='2', default_x=6.58, default_y=-74.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel')
                with Lyric(number='3', default_x=6.58, default_y=-97.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('geln')
            with Note(default_x=417.09, default_y=-557.77):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=407.03):
            with Note(default_x=19.34, default_y=-552.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mü')
                with Lyric(number='2', default_x=6.94, default_y=-74.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('grö')
                with Lyric(number='3', default_x=6.94, default_y=-97.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ste')
            with Note(default_x=286.74, default_y=-537.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-50.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
                with Lyric(number='2', default_x=9.01, default_y=-74.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer,')
                with Lyric(number='3', default_x=8.85, default_y=-97.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('hen.')
        with Measure(number='11', width=457.05):
            with Note(default_x=28.47, default_y=-537.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach')
                with Lyric(number='2', default_x=6.58, default_y=-74.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum')
                with Lyric(number='3', default_x=6.58, default_y=-97.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=150.46, default_y=-537.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.17, default_y=-50.68, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=6.58, default_y=-74.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin')
                with Lyric(number='3', default_x=6.58, default_y=-97.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=302.96, default_y=-547.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-74.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-97.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nun')
        with Measure(number='12', width=347.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(134.68)
            with Note(default_x=97.38, default_y=-545.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.14, default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text("wart'")
                with Lyric(number='2', default_x=6.58, default_y=-77.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('je')
                with Lyric(number='3', default_x=6.58, default_y=-101.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=185.73, default_y=-565.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                    Extend()
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der')
                with Lyric(number='3', default_y=-101.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('voll')
            with Note(default_x=246.48, default_y=-560.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=265.53):
            with Note(default_x=33.02, default_y=-545.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.19, default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich,')
                with Lyric(number='2', default_x=6.58, default_y=-77.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('zeit')
                with Lyric(number='3', default_x=8.8, default_y=-101.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('bracht,')
            with Note(default_x=98.99, default_y=-545.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text("Komm'")
                    Extend()
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
                    Extend()
                with Lyric(number='3', default_x=0.5, default_y=-101.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('drum,')
                    Extend()
            with Note(default_x=140.22, default_y=-540.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=181.46, default_y=-545.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=222.69, default_y=-550.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=293.05):
            with Note(default_x=35.81, default_y=-555.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('bald')
                    Extend()
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('zum')
                    Extend()
                with Lyric(number='3', default_y=-101.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt,')
                    Extend()
            with Note(default_x=163.63, default_y=-560.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=206.23, default_y=-555.57):
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
                with Lyric(number='1', default_x=6.58, default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='3', default_x=6.58, default_y=-101.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=248.84, default_y=-565.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=228.13):
            with Note(default_x=20.45, default_y=-550.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-54.43, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('let')
                    Extend()
                with Lyric(number='3', default_y=-101.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=83.86, default_y=-560.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=163.12, default_y=-545.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-77.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-101.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('ter')
        with Measure(number='16', width=218.1):
            with Note(default_x=31.7, default_y=-555.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-54.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich,')
                    Extend()
                with Lyric(number='2', default_y=-77.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('reit,')
                    Extend()
                with Lyric(number='3', default_y=-101.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht')
                    Extend()
            with Note(default_x=117.5, default_y=-560.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.5, default_y=-565.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=183.5, default_y=-535.57):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=377.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(132.73)
            with Note(default_x=97.38, default_y=-519.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.9, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("drück'")
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=176.84, default_y=-529.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('schließ')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
            with Note(default_x=276.16, default_y=-519.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
        with Measure(number='18', width=271.18):
            with Note(default_x=12.0, default_y=-514.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Au')
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind')
                    Extend()
            with Note(default_x=54.93, default_y=-519.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=97.86, default_y=-524.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=140.79, default_y=-529.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.72, default_y=-524.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                    Extend()
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                    Extend()
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('schon')
                    Extend()
        with Measure(number='19', width=226.85):
            with Note(default_x=14.0, default_y=-524.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.36, default_y=-529.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='2', default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
                with Lyric(number='3', default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu,')
                    Extend()
            with Note(default_x=112.08, default_y=-534.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.8, default_y=-529.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=187.53, default_y=-539.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=277.9):
            with Note(default_x=33.65, default_y=-524.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.17, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='2', default_x=11.17, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
                with Lyric(number='3', default_x=11.17, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text("komm',")
            with Note(default_x=114.54, default_y=-519.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='2', default_x=8.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
                with Lyric(number='3', default_x=8.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text("sel'")
            with Note(default_x=195.42, default_y=-519.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                with Lyric(number='2', default_x=6.58, default_y=-66.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
                with Lyric(number='3', default_x=6.58, default_y=-90.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='21', width=199.26):
            with Note(default_x=23.3, default_y=-539.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.03, default_y=-43.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='2', default_x=9.03, default_y=-66.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
                with Lyric(number='3', default_x=9.03, default_y=-90.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward', times=3)