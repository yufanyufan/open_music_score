with ScorePartwise(version='3.1'):
    with Identification():
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.7)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2084.21)
            PageWidth(1473.68)
            with PageMargins(type='even'):
                LeftMargin(70.1754)
                RightMargin(70.1754)
                TopMargin(70.1754)
                BottomMargin(140.351)
            with PageMargins(type='odd'):
                LeftMargin(70.1754)
                RightMargin(70.1754)
                TopMargin(70.1754)
                BottomMargin(140.351)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('God is our Refuge and Strength', default_x=736.841, default_y=2014.04, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Motet KV 20', default_x=736.841, default_y=1943.86, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W.A. Mozart', default_x=1403.51, default_y=1914.04, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
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
                MidiProgram(53)
                Volume(78.7402)
                Pan(-68.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(65.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(30.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(-19.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=242.44):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(100.14)
                        RightMargin(0.0)
                    TopSystemDistance(240.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('3')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=107.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=164.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=193.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='2', width=188.23):
            with Note(default_x=16.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=73.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.96, default_y=-42.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=129.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='3', width=196.53):
            with Note(default_x=24.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=76.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=142.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='4', width=212.61):
            with Note(default_x=38.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=13.5, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='5', width=180.57):
            with Note(default_x=17.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=63.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=132.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='6', width=212.82):
            with Note(default_x=32.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-42.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=83.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='7', width=268.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.26)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=87.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
                    Extend()
            with Note(default_x=177.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=218.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='8', width=178.85):
            with Note(default_x=17.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='9', width=198.13):
            with Note(default_x=41.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-47.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=146.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note(default_x=109.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='11', width=126.71):
            with Note(default_x=16.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=84.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='12', width=116.47):
            with Note(default_x=21.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=84.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='13', width=130.67):
            with Note(default_x=20.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='14', width=130.54):
            with Note(default_x=21.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.75, default_y=-47.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=92.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='15', width=206.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.26)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=102.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
                    Extend()
            with Note(default_x=136.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=170.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='16', width=185.48):
            with Note(default_x=23.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=76.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('fiuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=130.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='17', width=183.11):
            with Note(default_x=29.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.86, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=127.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='18', width=204.61):
            with Note(default_x=29.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=133.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='19', width=128.49):
            with Note(default_x=21.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=87.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='20', width=100.49):
            with Note(default_x=17.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=68.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='21', width=84.76):
            with Note(default_x=15.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='22', width=118.19):
            with Note(default_x=15.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=84.29):
            with Note(default_x=15.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=5.75, default_y=-46.26, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble.', font_family='Times New Roman', font_size='11.1404')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=242.44):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(70.11)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('3')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='2', width=188.23):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='3', width=196.53):
            with Note(default_x=24.12, default_y=-160.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=109.7, default_y=-160.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=142.12, default_y=-160.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='4', width=212.61):
            with Note(default_x=41.32, default_y=-160.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=97.76, default_y=-125.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.68, default_y=-51.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=154.2, default_y=-130.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='5', width=180.57):
            with Note(default_x=17.59, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=93.24, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=132.28, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='6', width=212.82):
            with Note(default_x=32.32, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.82, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=115.57, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=147.46, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=179.34, default_y=-135.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='7', width=268.46):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.4)
            with Note(default_x=87.38, default_y=-155.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=177.73, default_y=-160.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=218.51, default_y=-165.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='8', width=178.85):
            with Note(default_x=20.28, default_y=-160.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=77.56, default_y=-160.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-56.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='9', width=198.13):
            with Note(default_x=41.32, default_y=-165.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-56.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=146.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note(default_x=109.95, default_y=-145.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='11', width=126.71):
            with Note(default_x=16.21, default_y=-145.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-56.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=84.14, default_y=-145.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='12', width=116.47):
            with Note(default_x=24.12, default_y=-145.4):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='13', width=130.67):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='14', width=130.54):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note(default_x=92.93, default_y=-135.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='15', width=206.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.11)
            with Note(default_x=99.42, default_y=-155.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=170.58, default_y=-155.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='16', width=185.48):
            with Note(default_x=20.17, default_y=-155.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='17', width=183.11):
            with Note(default_x=29.36, default_y=-145.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=127.04, default_y=-145.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='18', width=204.61):
            with Note(default_x=32.32, default_y=-145.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.82, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=99.8, default_y=-155.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=134.2, default_y=-140.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=168.6, default_y=-145.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='19', width=128.49):
            with Note(default_x=21.16, default_y=-150.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=87.14, default_y=-150.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='20', width=100.49):
            with Note(default_x=17.32, default_y=-140.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='21', width=84.76):
            with Note(default_x=15.32, default_y=-140.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='22', width=118.19):
            with Note(default_x=18.28, default_y=-140.11):
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
            with Note(default_x=52.99, default_y=-145.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Lyric(number='1', default_x=3.26, default_y=-46.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='23', width=84.29):
            with Note(default_x=15.71, default_y=-140.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=5.75, default_y=-46.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble.', font_family='Times New Roman', font_size='11.1404')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=242.44):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(97.65)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('3')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='2', width=188.23):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='3', width=196.53):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='4', width=212.61):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='5', width=180.57):
            with Note(default_x=17.59, default_y=-247.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-58.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=93.24, default_y=-247.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=132.28, default_y=-247.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-58.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-282.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=93.24, default_y=-282.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=132.28, default_y=-282.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='6', width=212.82):
            with Note(default_x=29.36, default_y=-247.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                with Lyric(number='1', default_x=3.26, default_y=-58.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Backup():
                Duration(6.0)
            with Note(default_x=29.36, default_y=-282.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('whole')
                Dot()
                Accidental('sharp')
        with Measure(number='7', width=268.46):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.4)
            with Note(default_x=87.38, default_y=-251.8):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.96, default_y=-55.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note(default_x=218.51, default_y=-266.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
            with Backup():
                Duration(6.0)
            with Note(default_x=87.74, default_y=-286.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('whole')
        with Measure(number='8', width=178.85):
            with Note(default_x=17.32, default_y=-256.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=128.7, default_y=-261.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='9', width=198.13):
            with Note(default_x=41.32, default_y=-266.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=92.93, default_y=-271.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=144.55, default_y=-276.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='10', width=146.23):
            with Note(default_x=41.32, default_y=-276.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.54, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=126.71):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='12', width=116.47):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note(default_x=84.38, default_y=-266.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='13', width=130.67):
            with Note(default_x=20.17, default_y=-271.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-55.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=88.1, default_y=-276.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='14', width=130.54):
            with Note(default_x=24.12, default_y=-281.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-55.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='15', width=206.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.62)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='16', width=185.48):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='17', width=183.11):
            with Note(default_x=32.32, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=74.41, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=127.04, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='18', width=204.61):
            with Note(default_x=29.36, default_y=-255.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pr', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=133.84, default_y=-255.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='19', width=128.49):
            with Note(default_x=21.16, default_y=-255.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='20', width=100.49):
            with Note(default_x=17.32, default_y=-230.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='21', width=84.76):
            with Note(default_x=15.32, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='22', width=118.19):
            with Note(default_x=15.32, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Tied(type='stop')
        with Measure(number='23', width=84.29):
            with Note(default_x=15.71, default_y=-235.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=12.39, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble.', font_family='Times New Roman', font_size='11.1404')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=242.44):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(74.39)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('3')
                    BeatType('2')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='2', width=188.23):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='3', width=196.53):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='4', width=212.61):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='5', width=180.57):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='6', width=212.82):
            with Note():
                Rest(measure='yes')
                Duration(6.0)
                Voice('1')
        with Measure(number='7', width=268.46):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.99)
            with Note(default_x=87.38, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=177.73, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=218.51, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('our', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='8', width=178.85):
            with Note(default_x=20.64, default_y=-380.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=50.76, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.52, default_y=-390.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('fuge', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=128.7, default_y=-380.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='9', width=198.13):
            with Note(default_x=41.32, default_y=-375.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.54, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Strength,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=146.23):
            with Note(default_x=41.32, default_y=-400.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=75.64, default_y=-410.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=109.95, default_y=-375.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='11', width=126.71):
            with Note(default_x=16.21, default_y=-380.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=84.14, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='12', width=116.47):
            with Note(default_x=21.16, default_y=-390.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=84.38, default_y=-375.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='13', width=130.67):
            with Note(default_x=20.17, default_y=-380.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=88.1, default_y=-385.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='14', width=130.54):
            with Note(default_x=21.16, default_y=-390.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='15', width=206.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=99.42, default_y=-340.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                with Lyric(number='1', default_x=9.9, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='16', width=185.48):
            with Note(default_x=20.17, default_y=-335.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='17', width=183.11):
            with Note(default_x=32.32, default_y=-350.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.43, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble,', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=101.09, default_y=-365.73):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=127.4, default_y=-350.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=155.2, default_y=-355.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='18', width=204.61):
            with Note(default_x=29.36, default_y=-360.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=3.26, default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pre', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=133.84, default_y=-360.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('sent', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='19', width=128.49):
            with Note(default_x=21.16, default_y=-355.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('help', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='20', width=100.49):
            with Note(default_x=17.32, default_y=-355.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                with Lyric(number='1', default_x=3.26, default_y=-47.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='21', width=84.76):
            with Note(default_x=15.32, default_y=-350.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trou', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='22', width=118.19):
            with Note(default_x=15.32, default_y=-350.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Tied(type='stop')
        with Measure(number='23', width=84.29):
            with Note(default_x=15.71, default_y=-370.73):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=5.75, default_y=-47.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('ble.', font_family='Times New Roman', font_size='11.1404')
            with Barline(location='right'):
                BarStyle('light-heavy')