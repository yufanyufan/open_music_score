with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('48')
        WorkTitle('6 Lieder, Op.48')
    MovementNumber('3')
    MovementTitle('Vom Tode')
    with Identification():
        Creator('Ludwig van Beethoven', type='composer')
        Creator('Christian Fürchtegott Gellert', type='lyricist')
        Rights('OpenScore (CC0)')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.4)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2199.48)
            PageWidth(1556.0)
            with PageMargins(type='even'):
                LeftMargin(74.0741)
                RightMargin(74.0741)
                TopMargin(74.0741)
                BottomMargin(148.148)
            with PageMargins(type='odd'):
                LeftMargin(74.0741)
                RightMargin(74.0741)
                TopMargin(74.0741)
                BottomMargin(148.148)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditWords('6 Lieder, Op.48', default_x=777.999, default_y=2125.4, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditWords('3. Vom Tode', default_x=777.999, default_y=2125.4, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven', default_x=1481.92, default_y=1980.4, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Christian Fürchtegott Gellert', default_x=74.0741, default_y=1980.4, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('OpenScore (CC0)', default_x=777.999, default_y=148.148, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('OpenScore (CC0)', default_x=777.999, default_y=148.148, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Singstimme\nVoice')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Voice')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Pianoforte')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=193.79):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(163.23)
                        RightMargin(-0.0)
                    TopSystemDistance(242.52)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Mässig und eher langsam als geschwind', default_x=-40.16, relative_x=-33.86, relative_y=50.0, font_weight='bold', font_size='12')
                Sound(tempo=80.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='2', width=144.82):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=44.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mei')
            with Note(default_x=105.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='3', width=133.33):
            with Note(default_x=16.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=87.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bens')
        with Measure(number='4', width=127.24):
            with Note(default_x=21.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('zeit')
            with Note(default_x=85.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='5', width=130.81):
            with Note(default_x=27.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=8.97, default_y=-47.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('streicht,')
        with Measure(number='6', width=139.57):
            with Note(default_x=19.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stünd')
            with Note(default_x=92.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='7', width=113.24):
            with Note(default_x=13.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=8.28, default_y=-47.06, relative_y=-30.0):
                    Syllabic('single')
                    Text("eil'")
            with Note(default_x=74.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
        with Measure(number='8', width=128.34):
            with Note(default_x=22.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=86.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='9', width=133.48):
            with Note(default_x=26.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gra')
            with Note(default_x=91.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=9.03, default_y=-47.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
        with Measure(number='10', width=249.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.86)
                        RightMargin(0.0)
                    SystemDistance(140.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=155.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=201.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
        with Measure(number='11', width=151.47):
            with Note(default_x=39.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("ist's,")
            with Note(default_x=107.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='12', width=155.7):
            with Note(default_x=39.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=110.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('viel')
        with Measure(number='13', width=112.62):
            with Note(default_x=20.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=8.95, default_y=-50.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('leicht,')
            with Note(default_x=76.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=133.25):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=52.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=92.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
        with Measure(number='15', width=126.72):
            with Note(default_x=20.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('noch')
            with Note(default_x=85.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
        with Measure(number='16', width=127.8):
            with Note(default_x=17.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=84.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='17', width=125.88):
            with Note(default_x=16.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=83.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-50.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('be?')
        with Measure(number='18', width=107.75):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='19', width=96.71):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='20', width=172.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.86)
                        RightMargin(-0.0)
                    SystemDistance(140.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='21', width=101.26):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='22', width=126.45):
            with Note(default_x=28.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.95, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text("Denk',")
            with Note(default_x=88.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='23', width=151.49):
            with Note(default_x=39.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mensch,')
            with Note(default_x=107.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
        with Measure(number='24', width=119.95):
            with Note(default_x=18.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=79.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
        with Measure(number='25', width=103.15):
            with Note(default_x=22.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod!')
        with Measure(number='26', width=119.88):
            with Note(default_x=20.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Säu')
            with Note(default_x=80.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
        with Measure(number='27', width=143.16):
            with Note(default_x=20.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.93, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=95.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
        with Measure(number='28', width=121.26):
            with Note(default_x=20.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('Eins')
            with Note(default_x=81.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
        with Measure(number='29', width=107.55):
            with Note(default_x=26.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-50.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('Noth.')
        with Measure(number='30', width=119.88):
            with Note(default_x=20.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Säu')
            with Note(default_x=80.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
        with Measure(number='31', width=218.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.86)
                        RightMargin(0.0)
                    SystemDistance(140.0)
            with Note(default_x=115.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
                    Extend()
        with Measure(number='32', width=143.21):
            with Note(default_x=20.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=95.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
        with Measure(number='33', width=118.05):
            with Note(default_x=17.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Eins')
        with Measure(number='34', width=118.27):
            with Note(default_x=16.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
        with Measure(number='35', width=127.57):
            with Note(default_x=26.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Noth.')
        with Measure(number='36', width=136.67):
            with Note(default_x=17.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Säu')
            with Note(default_x=89.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
        with Measure(number='37', width=133.78):
            with Note(default_x=30.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
                    Extend()
        with Measure(number='38', width=144.67):
            with Note(default_x=17.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=94.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('denn')
        with Measure(number='39', width=124.74):
            with Note(default_x=24.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Eins')
        with Measure(number='40', width=121.28):
            with Note(default_x=20.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
        with Measure(number='41', width=224.94):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.86)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=103.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Noth.')
        with Measure(number='42', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='43', width=138.12):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='44', width=165.5):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='45', width=138.12):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='46', width=165.5):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='47', width=133.53):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='48', width=137.33):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
        with Measure(number='49', width=138.92):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=193.79):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(77.71)
                with StaffLayout(number=2):
                    StaffDistance(74.15)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=1.58, relative_y=-44.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=124.47, default_y=-177.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=124.47, default_y=-167.71):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=124.47, default_y=-152.71):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=124.47, default_y=-276.86):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=124.47, default_y=-266.86):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=124.47, default_y=-256.86):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=124.47, default_y=-241.86):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='2', width=144.82):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-43.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=44.84, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=105.52, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=133.33):
            with Note(default_x=16.55, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=87.57, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=127.24):
            with Note(default_x=21.0, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=85.53, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='5', width=130.81):
            with Note(default_x=27.81, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=40.39, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=90.35, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.22, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='6', width=139.57):
            with Note(default_x=19.31, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=31.9, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=92.47, default_y=-152.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=104.33, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=113.24):
            with Note(default_x=13.64, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=13.64, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=74.08, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=74.08, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=128.34):
            with Note(default_x=22.44, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=22.44, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=22.44, default_y=-132.71):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=86.77, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.77, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.77, default_y=-137.71):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=22.44, default_y=-246.86):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=22.44, default_y=-236.86):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=86.77, default_y=-246.86):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=86.77, default_y=-236.86):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=133.48):
            with Note(default_x=26.39, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=26.39, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=26.39, default_y=-137.71):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=91.45, default_y=-157.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.45, default_y=-147.71):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.32, default_y=-142.71):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=26.39, default_y=-256.86):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=26.39, default_y=-246.86):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=26.39, default_y=-236.86):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=91.45, default_y=-256.86):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=91.45, default_y=-246.86):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=91.45, default_y=-236.86):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=249.07):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.41)
                with StaffLayout(number=2):
                    StaffDistance(69.73)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-88.6)
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=155.01, default_y=-196.41):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=155.01, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=201.24, default_y=-196.41):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.24, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=108.41, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=108.41, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=108.41, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=201.24, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.24, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.24, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=151.47):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.91, relative_x=6.58, relative_y=-38.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=39.34, default_y=-176.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=39.34, default_y=-141.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.5, default_y=-171.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.5, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=39.34, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=39.34, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=26.75, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=39.34, default_y=-246.13):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=107.5, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=107.5, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.63, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=107.5, default_y=-246.13):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=155.7):
            with Note(default_x=39.34, default_y=-166.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=39.34, default_y=-131.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=110.1, default_y=-196.41):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=110.1, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=39.34, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=39.34, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=26.75, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=39.34, default_y=-246.13):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-261.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=112.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.96, relative_x=6.58, relative_y=-54.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=20.67, default_y=-196.41):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=20.67, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=76.41, default_y=-191.41):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.41, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=20.67, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=76.41, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.41, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=133.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=52.51, default_y=-191.41):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.51, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.08, default_y=-191.41):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.08, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=12.58, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=12.58, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=92.08, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=92.08, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=126.72):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-81.56)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-81.56)
                Staff(1)
            with Note(default_x=20.67, default_y=-191.41):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=85.09, default_y=-171.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=85.09, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=20.67, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=85.09, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=85.09, default_y=-246.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=127.8):
            with Note(default_x=17.59, default_y=-166.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.59, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=84.57, default_y=-161.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=96.43, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=17.59, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=84.57, default_y=-266.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.57, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=125.88):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.56, relative_x=6.58, relative_y=-41.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=16.87, default_y=-176.41):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-151.41):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=83.11, default_y=-186.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=16.87, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=16.87, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=83.11, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=107.75):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.83, relative_x=6.58, relative_y=-48.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-186.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=71.54, default_y=-186.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=71.54, default_y=-271.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='19', width=96.71):
            with Note(default_x=12.0, default_y=-171.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=63.29, default_y=-166.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(3.0)
            with Note(default_x=12.0, default_y=-291.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-271.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-256.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=63.29, default_y=-286.13):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.29, default_y=-271.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.29, default_y=-251.13):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=172.96):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.76)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=99.61, default_y=-138.76):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=143.9, default_y=-148.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=99.61, default_y=-253.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=99.61, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=99.61, default_y=-218.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=143.9, default_y=-263.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.9, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.9, default_y=-228.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='21', width=101.26):
            with Note(default_x=20.67, default_y=-153.76):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=69.42, default_y=-163.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-268.76):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-233.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=69.42, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=69.42, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='22', width=126.45):
            with Note(default_x=28.81, default_y=-163.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=88.05, default_y=-163.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=28.81, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=28.81, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=88.05, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.05, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='23', width=151.49):
            with Note(default_x=39.32, default_y=-148.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.5, default_y=-143.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=39.32, default_y=-263.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=39.32, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=39.32, default_y=-228.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=107.5, default_y=-258.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=107.5, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=107.5, default_y=-223.76):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=119.95):
            with Note(default_x=18.12, default_y=-138.76):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=79.94, default_y=-148.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=18.12, default_y=-253.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=18.12, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=18.12, default_y=-218.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=79.94, default_y=-263.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.94, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.94, default_y=-228.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='25', width=103.15):
            with Note(default_x=22.56, default_y=-163.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=22.56, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=22.56, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=71.31, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=71.31, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='26', width=119.88):
            with Note(default_x=20.67, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=80.88, default_y=-278.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=80.88, default_y=-243.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='27', width=143.16):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-91.56)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-91.56)
                Staff(1)
            with Note(default_x=20.67, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-158.76):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=33.26, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=95.2, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=95.2, default_y=-158.76):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.07, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-283.76):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-248.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=95.2, default_y=-283.76):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=95.2, default_y=-248.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='28', width=121.26):
            with Note(default_x=20.67, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-158.76):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=33.26, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=81.73, default_y=-178.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=81.73, default_y=-158.76):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=93.59, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-283.76):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-248.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=81.73, default_y=-283.76):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.73, default_y=-248.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='29', width=107.55):
            with Note(default_x=26.96, default_y=-173.76):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.96, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.96, default_y=-148.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=26.96, default_y=-288.76):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=26.96, default_y=-253.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=75.71, default_y=-288.76):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.71, default_y=-253.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='30', width=119.88):
            with Note(default_x=20.67, default_y=-173.76):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-143.76):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-173.76):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.88, default_y=-143.76):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-59.26, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=20.67, default_y=-288.76):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-253.76):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=80.88, default_y=-288.76):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=80.88, default_y=-253.76):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='31', width=218.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.62)
                with StaffLayout(number=2):
                    StaffDistance(70.16)
            with Note(default_x=115.45, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=115.45, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=115.45, default_y=-152.62):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=115.45, default_y=-142.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(3.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.15, relative_x=-13.42, relative_y=11.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=16.15)
                Staff(2)
            with Note(default_x=115.45, default_y=-292.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=115.45, default_y=-257.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=178.18, default_y=-292.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=178.18, default_y=-257.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='32', width=143.21):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-54.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=20.67, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-152.62):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-142.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=95.23, default_y=-167.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=95.23, default_y=-157.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=95.23, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-292.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-257.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=95.23, default_y=-287.78):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=95.23, default_y=-252.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='33', width=118.05):
            with Note(default_x=17.44, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.43, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=17.44, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=17.44, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=78.51, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.51, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='34', width=118.27):
            with Note(default_x=16.87, default_y=-152.62):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=16.87, default_y=-177.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=16.87, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=78.42, default_y=-167.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=16.87, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=16.87, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=78.42, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.42, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='35', width=127.57):
            with Note(default_x=26.96, default_y=-182.62):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.96, default_y=-172.62):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.96, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=26.96, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=26.96, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=88.03, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.03, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=136.67):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-86.56)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-86.56)
                Staff(1)
            with Note(default_x=17.44, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=89.97, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=89.97, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=89.97, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=17.44, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=17.44, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=89.97, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=89.97, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=133.78):
            with Note(default_x=30.47, default_y=-167.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=43.06, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=30.47, default_y=-142.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(3.0)
            with Note(default_x=30.47, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=30.47, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=93.2, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.2, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='38', width=144.67):
            with Note(default_x=17.44, default_y=-167.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-157.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-142.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-50.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=94.89, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.76, default_y=-167.62):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=94.89, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=17.44, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=17.44, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=94.89, default_y=-277.78):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=94.89, default_y=-242.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='39', width=124.74):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-48.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=24.13, default_y=-172.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=24.13, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=24.13, default_y=-147.62):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=24.13, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=24.13, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=85.2, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.2, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='40', width=121.28):
            with Note(default_x=20.67, default_y=-177.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-162.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=20.67, default_y=-152.62):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=20.67, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.67, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=81.74, default_y=-282.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.74, default_y=-247.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='41', width=224.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(98.75)
            with Note(default_x=103.41, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=103.41, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=103.41, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=103.41, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=103.41, default_y=-288.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=177.35, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='42', width=145.03):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=101.01, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=101.01, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=101.01, default_y=-258.75):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=101.01, default_y=-248.75):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Forward():
                Duration(2.0)
            with Note(default_x=101.01, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=138.12):
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-253.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note(default_x=15.8, default_y=-243.75):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=90.23, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='44', width=165.5):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=114.65, default_y=-263.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=126.52, default_y=-258.75):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=114.65, default_y=-248.75):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.65, default_y=-238.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=114.65, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=138.12):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-268.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=15.8, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-243.75):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=90.23, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='46', width=165.5):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=114.65, default_y=-273.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=114.65, default_y=-263.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=126.52, default_y=-258.75):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=114.65, default_y=-248.75):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=114.65, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='47', width=133.53):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-278.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=15.8, default_y=-268.75):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=87.4, default_y=-278.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=87.4, default_y=-268.75):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=87.4, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=87.4, default_y=-288.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='48', width=137.33):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-278.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-268.75):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=89.74, default_y=-278.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=89.74, default_y=-268.75):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=89.74, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-303.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-288.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=89.74, default_y=-313.75):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.74, default_y=-288.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='49', width=138.92):
            with Note():
                Rest(measure='yes')
                Duration(3.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-278.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
            with Note(default_x=15.8, default_y=-268.75):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-253.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(3.0)
            with Note(default_x=15.8, default_y=-323.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(3.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-97.15, relative_y=-10.0)
            with Note(default_x=15.8, default_y=-288.75):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')