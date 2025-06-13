with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('48')
        WorkTitle('6 Lieder, Op.48')
    MovementNumber('5')
    MovementTitle('Gottes Macht und Vorsehung')
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
        CreditWords('6 Lieder, Op.48 ', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditWords('5. Gottes Macht und Vorsehung', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven', default_x=1134.19, default_y=1480.67, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Christian Fürchtegott Gellert', default_x=56.6929, default_y=1480.67, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('OpenScore (CC0)', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
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
        with Measure(number='1', width=189.64):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(173.4)
                        RightMargin(0.0)
                    TopSystemDistance(234.41)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Mit Kraft und Feuer', default_x=-44.43, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=140.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=138.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
        with Measure(number='2', width=135.44):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=74.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='3', width=135.19):
            with Note(default_x=25.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.88, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lied!')
            with Note(default_x=103.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='4', width=162.73):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=124.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='5', width=137.69):
            with Note(default_x=24.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=80.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='6', width=143.4):
            with Note(default_x=22.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Stär')
            with Note(default_x=75.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.06, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=233.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=102.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hehr')
            with Note(default_x=145.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=188.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein')
        with Measure(number='8', width=163.41):
            with Note(default_x=26.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=7.89, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text("Nam'")
            with Note(default_x=128.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=210.18):
            with Note(default_x=18.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=81.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.63, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind\xa0')
            with Note(default_x=113.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
            with Note(default_x=175.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='10', width=175.19):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wer')
            with Note(default_x=56.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=134.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='11', width=127.05):
            with Note(default_x=12.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=94.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
        with Measure(number='12', width=147.59):
            with Note(default_x=15.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=101.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='13', width=209.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein')
            with Note(default_x=133.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
        with Measure(number='14', width=184.43):
            with Note(default_x=21.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.99, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('biet.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
        with Measure(number='15', width=163.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=193.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=168.37):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=137.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=189.64):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(85.25)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-52.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=138.26, default_y=-175.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=138.26, default_y=-140.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.22, relative_x=6.58, relative_y=-49.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=85.88, default_y=-295.25):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=85.88, default_y=-260.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=135.44):
            with Note(default_x=15.8, default_y=-180.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-145.25):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=74.64, default_y=-155.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.84, default_y=-275.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=12.84, default_y=-240.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=135.19):
            with Note(default_x=25.2, default_y=-185.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=25.2, default_y=-150.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=103.58, default_y=-180.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.58, default_y=-145.25):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=25.2, default_y=-275.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=25.2, default_y=-240.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=73.21, default_y=-280.25):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=73.21, default_y=-245.25):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=162.73):
            with Note(default_x=15.8, default_y=-175.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-140.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=124.89, default_y=-170.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=124.89, default_y=-135.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.16, default_y=-285.25):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=16.16, default_y=-250.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=52.4, default_y=-290.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=52.4, default_y=-255.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.65, default_y=-295.25):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.65, default_y=-260.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=124.89, default_y=-300.25):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=124.89, default_y=-265.25):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=137.69):
            with Note(default_x=24.66, default_y=-165.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=24.66, default_y=-140.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=24.66, default_y=-130.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=80.19, default_y=-160.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=80.19, default_y=-140.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=80.19, default_y=-125.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=21.7, default_y=-305.25):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=21.7, default_y=-270.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='6', width=143.4):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-48.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=22.46, default_y=-155.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=22.46, default_y=-145.25):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=22.46, default_y=-120.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=75.7, default_y=-155.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.46, default_y=-310.25):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=22.46, default_y=-275.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=75.7, default_y=-275.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.7, default_y=-240.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='7', width=233.07):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(82.75)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-26.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=102.7, default_y=-122.75):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.62, default_y=-132.75):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=188.55, default_y=-142.75):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(8.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=163.41):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.25, relative_x=6.58, relative_y=-53.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=26.38, default_y=-187.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.38, default_y=-167.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=26.38, default_y=-152.75):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=128.05, default_y=-182.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.05, default_y=-172.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.05, default_y=-157.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.51, default_y=-297.75):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=94.28, default_y=-262.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.05, default_y=-267.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=210.18):
            with Note(default_x=18.62, default_y=-177.75):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.62, default_y=-162.75):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=81.18, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=81.18, default_y=-132.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=113.24, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=113.24, default_y=-132.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=175.8, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=175.8, default_y=-132.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=18.62, default_y=-272.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=81.18, default_y=-237.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=81.18, default_y=-227.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=113.24, default_y=-237.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=113.24, default_y=-227.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=175.8, default_y=-237.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=175.8, default_y=-227.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=175.19):
            with Note(default_x=17.23, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-132.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.32, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.32, default_y=-137.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=134.5, default_y=-137.75):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-237.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-227.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.32, default_y=-232.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.32, default_y=-222.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='11', width=127.05):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.95, relative_x=3.29, relative_y=-45.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=12.46, default_y=-157.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=12.46, default_y=-122.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=94.17, default_y=-157.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=94.17, default_y=-122.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-49.0):
                        Ff()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=62.88, default_y=-267.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.88, default_y=-257.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.88, default_y=-242.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.88, default_y=-232.75):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.17, default_y=-267.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.17, default_y=-257.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.17, default_y=-242.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.17, default_y=-232.75):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=147.59):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.95, relative_x=3.29, relative_y=-44.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=15.46, default_y=-157.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.46, default_y=-122.75):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=101.88, default_y=-162.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=101.88, default_y=-127.75):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.46, default_y=-262.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=15.46, default_y=-252.75):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=15.46, default_y=-237.75):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=15.46, default_y=-227.75):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=101.88, default_y=-257.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.88, default_y=-247.75):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.88, default_y=-237.75):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.88, default_y=-222.75):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=209.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.15)
                with StaffLayout(number=2):
                    StaffDistance(72.4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=4.58, relative_y=-42.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=59.77, default_y=-163.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=59.77, default_y=-128.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=133.53, default_y=-173.15):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=133.53, default_y=-163.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=133.53, default_y=-153.15):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=146.12, default_y=-148.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=59.77, default_y=-275.55):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=59.77, default_y=-265.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=59.77, default_y=-250.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=59.77, default_y=-240.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=133.53, default_y=-270.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=133.53, default_y=-260.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=133.53, default_y=-250.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=133.53, default_y=-235.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=184.43):
            with Note(default_x=21.97, default_y=-168.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.97, default_y=-158.15):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.97, default_y=-148.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.97, default_y=-133.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.18, default_y=-168.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.18, default_y=-133.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-46.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=102.04, default_y=-148.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=102.04, default_y=-113.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.61, default_y=-290.55):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=21.61, default_y=-255.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=142.61, default_y=-280.55):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=142.61, default_y=-245.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=163.42):
            with Note(default_x=12.36, default_y=-148.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-113.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.73, default_y=-178.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=49.73, default_y=-143.15):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.73, default_y=-153.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=86.73, default_y=-118.15):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(8.0)
            with Note(default_x=12.0, default_y=-275.55):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-240.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=124.46, default_y=-285.55):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=124.46, default_y=-250.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=193.56):
            with Note(default_x=15.8, default_y=-153.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-118.15):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.84, default_y=-158.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.84, default_y=-123.15):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.88, default_y=-143.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=103.88, default_y=-133.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=115.75, default_y=-128.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=147.92, default_y=-153.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.92, default_y=-138.15):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=147.92, default_y=-128.15):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-295.55):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-260.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=59.84, default_y=-290.55):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.84, default_y=-255.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=103.88, default_y=-310.55):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=103.88, default_y=-275.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=147.92, default_y=-305.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.92, default_y=-270.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='17', width=168.37):
            with Note(default_x=15.8, default_y=-158.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-148.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-133.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=91.29, default_y=-163.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.29, default_y=-148.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.29, default_y=-138.15):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-290.55):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-255.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=91.29, default_y=-305.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.29, default_y=-270.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='18', width=137.46):
            with Note(default_x=15.8, default_y=-158.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.8, default_y=-148.15):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.8, default_y=-133.15):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-290.55):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.8, default_y=-255.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')