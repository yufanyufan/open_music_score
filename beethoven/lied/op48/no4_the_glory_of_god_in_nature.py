with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Die Ehre Gottes aus der Natur')
    with Identification():
        Creator('L. van Beethoven', type='composer')
        Rights('für gemischten Chor bearbeitet von Viktor Janitzek')
        with Encoding():
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
            PageHeight(1683.28)
            PageWidth(1190.82)
            with PageMargins(type='even'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(85.034)
            with PageMargins(type='odd'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(85.034)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Die Ehre Gottes aus der Natur', default_x=595.408, default_y=1626.59, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('L. van Beethoven (1770 - 1827)', default_x=1134.13, default_y=1526.59, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('C.F.Gellert (1715 - 1769)', default_x=56.6894, default_y=1526.59, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('für gemischten Chor bearbeitet von Viktor Janitzek', default_x=595.408, default_y=85.034, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('für gemischten Chor bearbeitet von Viktor Janitzek', default_x=595.408, default_y=85.034, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('S\nA')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano/Alto')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(-21.0)
        with ScorePart(id='P2'):
            PartName('T\nB')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Tenor/Bass')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(21.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=159.22):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.4)
                        RightMargin(-0.0)
                    TopSystemDistance(175.8)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction():
                with DirectionType():
                    Words('Majestätisch und erhaben', default_y=55.8, relative_y=20.0, font_size='12')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=7.55, relative_x=-45.88, relative_y=26.09):
                        BeatUnit('quarter')
                        PerMinute('76')
                with DirectionType():
                    Words('\n', default_x=-37.31, default_y=7.55, relative_x=-45.88, relative_y=26.09, font_weight='bold', font_size='12')
                    Words(None)
                Sound(tempo=76.0)
            with Note(default_x=111.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-14.1, default_y=-72.95, relative_y=-35.0):
                    Syllabic('single')
                    Text('1.Die')
                with Lyric(number='2', default_x=-16.1, default_y=-98.86, relative_y=-35.0):
                    Syllabic('begin')
                    Text('2.Ver')
            with Backup():
                Duration(2.0)
            with Note(default_x=111.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='1', width=143.45):
            with Note(default_x=36.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('end')
                    Text("nimm's")
            with Note(default_x=89.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
            with Backup():
                Duration(8.0)
            with Note(default_x=36.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=89.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='2', width=148.41):
            with Note(default_x=19.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('begin')
                    Text('rüh')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('begin')
                    Text('sie')
            with Note(default_x=76.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-72.95, relative_y=-35.0):
                    Syllabic('end')
                    Text('men')
                with Lyric(number='2', default_x=6.58, default_y=-98.86, relative_y=-35.0):
                    Syllabic('end')
                    Text('he')
            with Note(default_x=111.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-72.95, relative_y=-35.0):
                    Syllabic('single')
                    Text('des')
                with Lyric(number='2', default_x=6.58, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('die')
            with Backup():
                Duration(8.0)
            with Note(default_x=19.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=76.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=154.77):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.4, relative_y=30.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=26.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('begin')
                    Text('E')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Wun')
            with Note(default_x=82.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-72.95, relative_y=-35.0):
                    Syllabic('middle')
                    Text('wi')
                with Lyric(number='2', default_x=6.58, default_y=-98.86, relative_y=-35.0):
                    Syllabic('end')
                    Text('der')
            with Note(default_x=118.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-72.95, relative_y=-35.0):
                    Syllabic('end')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
            with Backup():
                Duration(8.0)
            with Note(default_x=26.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=82.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=141.87):
            with Note(default_x=24.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Eh')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Wer')
            with Note(default_x=66.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                    with Articulations():
                        Caesura(None)
                with Lyric(number='1', default_x=8.71, default_y=-72.95, relative_y=-35.0):
                    Syllabic('end')
                    Text('re,')
                with Lyric(number='2', default_x=8.66, default_y=-98.86, relative_y=-35.0):
                    Syllabic('end')
                    Text('ke,')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=110.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-72.95, relative_y=-35.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='2', default_x=6.58, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('die')
            with Backup():
                Duration(8.0)
            with Note(default_x=24.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=66.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=110.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=166.13):
            with Note(default_x=31.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('single')
                    Text('Schall')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=97.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('single')
                    Text('pflanzt')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('single')
                    Text('so')
            with Backup():
                Duration(8.0)
            with Note(default_x=31.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=97.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='6', width=130.18):
            with Note(default_x=22.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('begin')
                    Text('sei')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=75.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-72.95, relative_y=-35.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='2', default_x=6.22, default_y=-98.86, relative_y=-35.0):
                    Syllabic('end')
                    Text('lich')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=75.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='7', width=253.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(103.53)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=99.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-73.35, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Na')
                with Lyric(number='2', default_x=6.22, default_y=-99.26, relative_y=-35.0):
                    Syllabic('begin')
                    Text('auf')
            with Note(default_x=163.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('end')
                    Text('men')
                with Lyric(number='2', default_y=-99.26, relative_y=-35.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=218.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=99.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=162.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='8', width=158.98):
            with Note(default_x=25.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
                with Lyric(number='1', default_x=8.42, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('fort.')
                with Lyric(number='2', default_x=9.21, default_y=-99.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('stellt!')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=112.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('Ihn')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Ver')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=112.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=156.57):
            with Note(default_x=22.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('rühmt')
                with Lyric(number='2', default_x=6.22, default_y=-99.26, relative_y=-35.0):
                    Syllabic('middle')
                    Text('kün')
            with Note(default_x=110.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('digt')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=110.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=224.67):
            with Note(default_x=27.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-73.35, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Erd')
                with Lyric(number='2', default_x=6.22, default_y=-99.26, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Weis')
            with Note(default_x=114.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('end')
                    Text('kreis,')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=168.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('ihn')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=114.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=168.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=277.79):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
            with Note(default_x=22.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-73.35, relative_y=-35.0):
                    Syllabic('begin')
                    Text('prei')
                with Lyric(number='2', default_x=6.22, default_y=-99.26, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Ord')
            with Note(default_x=135.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('end')
                    Text('sen')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('nung')
            with Note(default_x=205.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-99.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=135.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=217.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='12', width=234.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(-0.0)
                    SystemDistance(133.78)
            with Note(default_x=99.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-66.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Mee')
                with Lyric(number='2', default_x=6.22, default_y=-92.66, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Stä')
            with Note(default_x=159.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.11, default_y=-66.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('re;')
                with Lyric(number='2', default_x=8.66, default_y=-92.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('ke,')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=10.5, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=45.5)
            with Note(default_x=195.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('dir')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=112.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=159.19, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=111.63):
            with Note(default_x=21.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=8.45, default_y=-66.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('nimm,')
                with Lyric(number='2', default_x=6.22, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('nicht')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=69.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.22, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('den')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=69.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='14', width=125.93):
            with Note(default_x=30.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=8.08, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('Mensch,')
                with Lyric(number='2', default_x=8.32, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Herrn,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=92.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('den')
            with Backup():
                Duration(8.0)
            with Note(default_x=30.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=92.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=117.43):
            with Note(default_x=30.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_x=6.22, default_y=-66.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('gött')
                with Lyric(number='2', default_x=6.22, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Herrn')
            with Note(default_x=74.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_x=6.22, default_y=-66.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('lich')
                with Lyric(number='2', default_x=6.22, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
            with Backup():
                Duration(8.0)
            with Note(default_x=30.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=74.75, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='16', width=148.5):
            with Note(default_x=27.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.1, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('Wort!')
                with Lyric(number='2', default_x=10.77, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Welt?')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=99.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('Wer')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Kannst')
        with Measure(number='17', width=98.34):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('trägt')
                with Lyric(number='2', default_x=6.94, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=58.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-66.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.94, default_y=-92.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='18', width=126.44):
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('Wer\n', default_y=37.4, relative_y=40.0, font_size='11')
                    Words('Kannst')
            with Note(default_x=96.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-66.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.94, default_y=-92.66, relative_y=-35.0):
                    Syllabic('begin')
                    Text('We')
            with Note(default_x=67.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('sen')
            with Note(default_x=96.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('begin')
                    Text('un')
        with Measure(number='19', width=108.64):
            with Direction(placement='above'):
                with DirectionType():
                    Words('trägt\n', relative_x=10.59, relative_y=57.84, font_size='11')
                    Words('du')
            with Note(default_x=21.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('der\n', default_y=26.4, relative_y=40.0, font_size='11')
                    Words('der')
            with Note(default_x=81.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-66.75, relative_y=-35.0):
                    Syllabic('middle')
                    Text('zähl')
                with Lyric(number='2', default_x=6.94, default_y=-92.66, relative_y=-35.0):
                    Syllabic('middle')
                    Text('zähl')
            with Note(default_x=58.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-66.75, relative_y=-35.0):
                    Syllabic('middle')
                    Text('ba')
                with Lyric(number='2', default_x=6.58, default_y=-92.66, relative_y=-35.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=81.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=2.45, default_y=-66.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=2.45, default_y=-92.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='20', width=477.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(121.9)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Him-\n', default_y=26.0, relative_y=40.0, font_size='11')
                    Words('We-')
            with Note(default_x=105.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('mel\n', default_y=27.65, relative_y=40.0, font_size='11')
                    Words('sen')
            with Note(default_x=187.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('un-\n', default_y=22.45, relative_y=40.0, font_size='11')
                    Words('un-')
            with Note(default_x=238.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('zähl-\n', default_y=26.4, relative_y=40.0, font_size='11')
                    Words('zähl-')
            with Note(default_x=290.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('ba-\n', default_y=22.65, relative_y=40.0, font_size='11')
                    Words('ba-')
            with Note(default_x=372.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('re\n', default_y=13.7, relative_y=40.0, font_size='11')
                    Words('re')
            with Note(default_x=423.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=104.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-76.2, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Ster')
                with Lyric(number='2', default_x=6.94, default_y=-102.11, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Hee')
            with Note(default_x=290.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.72, default_y=-76.2, relative_y=-35.0):
                    Syllabic('end')
                    Text('ne,')
                with Lyric(number='2', default_x=8.71, default_y=-102.11, relative_y=-35.0):
                    Syllabic('end')
                    Text('re,')
            with Note(default_x=372.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('begin')
                    Text('un')
        with Measure(number='21', width=135.16):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Ster-\n', default_y=18.5, relative_y=40.0, font_size='11')
                    Words('Hee-')
            with Note(default_x=23.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('ne?\n', relative_x=12.35, relative_y=59.61, font_size='11')
                    Words('re.')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=50.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-76.2, relative_y=-35.0):
                    Syllabic('middle')
                    Text('zähl')
                with Lyric(number='2', default_x=6.94, default_y=-102.11, relative_y=-35.0):
                    Syllabic('middle')
                    Text('zähl')
            with Note(default_x=78.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('middle')
                    Text('ba')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('middle')
                    Text('ba')
            with Note(default_x=105.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('end')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='22', width=197.31):
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('Wer\n', default_y=6.85, relative_y=40.0, font_size='11')
                    Words('den')
            with Note(default_x=147.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-76.2, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Ster')
                with Lyric(number='2', default_x=6.94, default_y=-102.11, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Hee')
            with Note(default_x=99.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.12, default_y=-76.2, relative_y=-35.0):
                    Syllabic('end')
                    Text('ne?')
                with Lyric(number='2', default_x=8.71, default_y=-102.11, relative_y=-35.0):
                    Syllabic('end')
                    Text('re,')
            with Note(default_x=159.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=-5.28, default_y=-76.2, relative_y=-35.0):
                    Syllabic('single')
                    Text('Wer')
                with Lyric(number='2', default_x=-5.28, default_y=-102.11, relative_y=-35.0):
                    Syllabic('single')
                    Text('den')
        with Measure(number='23', width=261.75):
            with Direction(placement='above'):
                with DirectionType():
                    Words('führt\n', default_y=48.65, relative_y=40.0, font_size='11')
                    Words('klein         -')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
            with Note(default_x=18.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('die\n', default_y=48.65, relative_y=40.0, font_size='11')
                    Words('sten')
            with Note(default_x=199.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=18.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('single')
                    Text('führt')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('begin')
                    Text('klein')
            with Note(default_x=78.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('end')
                    Text('sten')
            with Note(default_x=139.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.41, default_y=-76.2, relative_y=-35.0):
                    Syllabic('single')
                    Text("Sonn'")
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('single')
                    Text('Staub')
            with Note(default_x=199.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-76.2, relative_y=-35.0):
                    Syllabic('single')
                    Text('aus')
                with Lyric(number='2', default_x=6.58, default_y=-102.11, relative_y=-35.0):
                    Syllabic('begin')
                    Text('fühl')
        with Measure(number='24', width=259.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(73.4)
            with Direction(placement='above'):
                with DirectionType():
                    Words("Sonn'\n", default_y=18.5, relative_y=40.0, font_size='11')
                    Words('Staub')
            with Note(default_x=102.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('aus\n', relative_x=3.53, relative_y=55.21, font_size='11')
                    Words('fühl-')
            with Note(default_x=151.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('ih-\n', relative_x=21.18, relative_y=59.86, font_size='11')
                    Words('los')
            with Note(default_x=176.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('rem\n', default_y=33.4, relative_y=40.0, font_size='11')
                    Words('be-')
            with Note(default_x=224.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=102.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-82.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('ih')
                with Lyric(number='2', default_x=6.94, default_y=-108.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('los')
            with Note(default_x=176.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-82.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('rem')
                with Lyric(number='2', default_y=-108.66, relative_y=-35.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=224.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=102.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=176.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=224.71, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='25', width=201.6):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Zelt?\n', relative_x=19.41, relative_y=55.41, font_size='11')
                    Words('schaun?')
            with Note(default_x=34.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=9.65, relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-46.95, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=34.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=11.57, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('Zelt?')
                with Lyric(number='2', default_x=11.6, default_y=-108.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('schaun?')
            with Note(default_x=144.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('Sie')
                with Lyric(number='2', default_x=6.58, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('Durch')
            with Backup():
                Duration(8.0)
            with Note(default_x=34.6, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('3')
                Type('quarter')
        with Measure(number='26', width=212.29):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=162.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=36.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.25, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('kommt,')
                with Lyric(number='2', default_x=9.17, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('wen,')
            with Note(default_x=162.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('sie')
                with Lyric(number='2', default_x=6.58, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('durch')
        with Measure(number='27', width=180.8):
            with Note(default_x=36.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=107.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=36.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('kommt')
                with Lyric(number='2', default_x=6.94, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('wen')
            with Note(default_x=107.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.94, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('ist')
        with Measure(number='28', width=217.46):
            with Note(default_x=28.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=111.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.4, relative_y=30.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=163.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=28.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-82.75, relative_y=-35.0):
                    Syllabic('begin')
                    Text('leuch')
                with Lyric(number='2', default_x=6.94, default_y=-108.66, relative_y=-35.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=111.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-82.75, relative_y=-35.0):
                    Syllabic('end')
                    Text('tet')
                with Lyric(number='2', default_x=11.03, default_y=-108.66, relative_y=-35.0):
                    Syllabic('end')
                    Text('les?')
            with Note(default_x=163.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-82.75, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-108.66, relative_y=-35.0):
                    Syllabic('single')
                    Text('O')
        with Measure(number='29', width=303.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
            with Note(default_x=88.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=183.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=242.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=88.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('lacht')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('gib')
            with Note(default_x=183.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='2', default_x=6.58, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('ihm')
            with Note(default_x=242.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('von')
                with Lyric(number='2', default_x=6.58, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='30', width=221.16):
            with Note(default_x=17.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
            with Note(default_x=98.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                    with Articulations():
                        Caesura(None)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=169.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('begin')
                    Text('fer')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('begin')
                    Text('Eh')
            with Note(default_x=98.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.72, default_y=-72.55, relative_y=-35.0):
                    Syllabic('end')
                    Text('ne,')
                with Lyric(number='2', default_x=9.31, default_y=-98.46, relative_y=-35.0):
                    Syllabic('end')
                    Text('re!')
            with Note(default_x=169.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=9.44, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('"Mir",')
        with Measure(number='31', width=176.04):
            with Note(default_x=25.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('läuft')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('ruft')
            with Note(default_x=99.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='32', width=224.31):
            with Note(default_x=25.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=155.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('Weg')
                with Lyric(number='2', default_x=9.02, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=155.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('gleich')
                with Lyric(number='2', default_x=2.93, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('"sollst')
        with Measure(number='33', width=146.01):
            with Note(default_x=16.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=80.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('als')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=80.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-72.55, relative_y=-35.0):
                    Syllabic('single')
                    Text('ein')
                with Lyric(number='2', default_x=6.94, default_y=-98.46, relative_y=-35.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='34', width=321.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=88.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=241.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=88.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('Held,')
                with Lyric(number='2', default_x=14.29, default_y=-94.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('traun!"')
            with Note(default_x=241.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=9.44, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('"Mir",')
        with Measure(number='35', width=182.96):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.4, relative_y=30.0):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.4)
            with Note(default_x=16.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=125.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('läuft')
                with Lyric(number='2', default_x=6.94, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('ruft')
            with Note(default_x=125.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='2', default_x=6.58, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='36', width=240.23):
            with Note(default_x=25.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=166.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('Weg')
                with Lyric(number='2', default_x=9.02, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=166.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('gleich')
                with Lyric(number='2', default_x=2.93, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('"sollst')
        with Measure(number='37', width=161.93):
            with Note(default_x=16.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=88.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('als')
                with Lyric(number='2', default_x=6.94, default_y=-94.26, relative_y=-35.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=88.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('ein')
                with Lyric(number='2', default_x=6.94, default_y=-94.26, relative_y=-35.0):
                    Syllabic('begin')
                    Text('ver')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=88.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
        with Measure(number='38', width=165.06):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=27.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=42.8, relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.68, default_y=-68.35, relative_y=-35.0):
                    Syllabic('single')
                    Text('Held.')
                with Lyric(number='2', default_x=14.29, default_y=-94.26, relative_y=-35.0):
                    Syllabic('end')
                    Text('traun!"')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('3')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=159.22):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(153.66)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=111.08, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(2.0)
            with Note(default_x=111.08, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='1', width=143.45):
            with Note(default_x=36.65, default_y=-188.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=89.07, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=36.65, default_y=-188.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=89.07, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='2', width=148.41):
            with Note(default_x=19.66, default_y=-213.66):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=76.37, default_y=-223.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.59, default_y=-188.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=19.66, default_y=-213.66):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=76.37, default_y=-223.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.59, default_y=-223.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=154.77):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.2, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=26.25, default_y=-188.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=82.86, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=118.02, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=26.25, default_y=-223.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=82.86, default_y=-228.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.02, default_y=-223.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=141.87):
            with Note(default_x=24.06, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=66.44, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=110.69, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=24.06, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=66.44, default_y=-238.66):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-64.65, relative_y=-10.0)
            with Note(default_x=110.69, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=166.13):
            with Note(default_x=31.25, default_y=-208.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=97.71, default_y=-183.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=31.25, default_y=-208.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=97.71, default_y=-218.66):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='6', width=130.18):
            with Note(default_x=22.86, default_y=-193.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=75.53, default_y=-203.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.86, default_y=-228.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=75.53, default_y=-238.66):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='7', width=253.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(150.96)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.7, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=99.98, default_y=-185.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=163.16, default_y=-190.96):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=218.86, default_y=-180.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=99.98, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=162.8, default_y=-235.96):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='8', width=158.98):
            with Note(default_x=25.47, default_y=-185.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=112.8, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.47, default_y=-220.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-53.4, relative_y=-10.0)
            with Note(default_x=112.8, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=156.57):
            with Note(default_x=22.45, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=110.18, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.45, default_y=-235.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=110.18, default_y=-235.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=224.67):
            with Note(default_x=27.05, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=114.37, default_y=-210.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.72, default_y=-195.96):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.05, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=114.37, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=168.72, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Accent()
        with Measure(number='11', width=277.79):
            with Note(default_x=22.06, default_y=-205.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-84.08, relative_x=-111.17)
            with Note(default_x=135.2, default_y=-205.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.7, default_y=-205.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=1.23)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.06, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=135.2, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=205.7, default_y=-230.96):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=234.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(155.04)
            with Note(default_x=99.98, default_y=-210.04):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.95, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=159.19, default_y=-210.04):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-81.95)
            with Note(default_x=195.97, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=99.98, default_y=-230.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=159.19, default_y=-230.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.97, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=111.63):
            with Note(default_x=21.63, default_y=-190.04):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=69.55, default_y=-190.04):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.63, default_y=-200.04):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=69.55, default_y=-210.04):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='14', width=125.93):
            with Note(default_x=30.39, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=92.35, default_y=-205.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=30.39, default_y=-205.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=92.35, default_y=-205.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=117.43):
            with Note(default_x=30.65, default_y=-190.04):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=74.75, default_y=-185.04):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=30.65, default_y=-225.04):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=74.75, default_y=-220.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Accent()
        with Measure(number='16', width=148.5):
            with Note(default_x=27.78, default_y=-205.04):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=99.72, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.78, default_y=-240.04):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-64.65, relative_y=-10.0)
            with Note(default_x=99.72, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='17', width=98.34):
            with Note(default_x=21.36, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=58.87, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=58.87, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='18', width=126.44):
            with Note(default_x=21.36, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=67.02, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.52, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=67.02, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=96.52, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=108.64):
            with Note(default_x=21.36, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=58.73, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.85, default_y=-195.04):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.36, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=58.73, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.85, default_y=-215.04):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=477.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(156.91)
            with Note(default_x=104.79, default_y=-196.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=290.28, default_y=-196.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=372.56, default_y=-191.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=104.79, default_y=-216.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=290.28, default_y=-216.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=372.56, default_y=-216.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=135.16):
            with Note(default_x=22.66, default_y=-186.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=78.29, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.93, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.66, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=78.29, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=105.93, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=197.31):
            with Note(default_x=22.46, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.66, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.68, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.46, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=99.66, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.68, default_y=-221.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=261.75):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=18.42, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.85, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.28, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=199.72, default_y=-206.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=18.42, default_y=-226.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.85, default_y=-226.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.28, default_y=-226.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.72, default_y=-226.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=259.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(178.25)
            with Note(default_x=102.59, default_y=-233.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=176.11, default_y=-233.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=102.59, default_y=-258.25):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=176.11, default_y=-258.25):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='25', width=201.6):
            with Note(default_x=34.6, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.4, relative_y=30.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=144.07, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=34.6, default_y=-263.25):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-64.65, relative_y=-10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
        with Measure(number='26', width=212.29):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-99.65)
            with Note(default_x=36.34, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=162.36, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=162.36, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=180.8):
            with Note(default_x=36.45, default_y=-213.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=107.65, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=36.45, default_y=-213.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=107.65, default_y=-228.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='28', width=217.46):
            with Note(default_x=28.25, default_y=-238.25):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=111.83, default_y=-248.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.2, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=163.85, default_y=-213.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=28.25, default_y=-238.25):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=111.83, default_y=-248.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.85, default_y=-248.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='29', width=303.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(153.91)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.8)
            with Note(default_x=88.78, default_y=-188.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=183.79, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=242.95, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=88.78, default_y=-223.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=183.79, default_y=-228.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=242.95, default_y=-223.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=221.16):
            with Note(default_x=17.86, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=98.68, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=169.27, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=17.86, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=98.68, default_y=-238.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-64.65, relative_y=-10.0)
            with Note(default_x=169.27, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=176.04):
            with Note(default_x=25.45, default_y=-208.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=99.77, default_y=-183.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-208.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=99.77, default_y=-218.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='32', width=224.31):
            with Note(default_x=25.45, default_y=-193.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=155.99, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-228.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=155.99, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='33', width=146.01):
            with Note(default_x=16.26, default_y=-188.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=80.15, default_y=-193.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.26, default_y=-198.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=80.15, default_y=-203.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='34', width=321.04):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(152.81)
            with Note(default_x=88.78, default_y=-187.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=241.4, default_y=-187.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=88.78, default_y=-222.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=241.4, default_y=-187.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=182.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=16.45, default_y=-187.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
            with Note(default_x=125.6, default_y=-187.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.45, default_y=-197.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=125.6, default_y=-197.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=240.23):
            with Note(default_x=25.45, default_y=-182.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=166.52, default_y=-182.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=25.45, default_y=-217.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=166.52, default_y=-207.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=161.93):
            with Note(default_x=16.26, default_y=-177.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.45, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=88.11, default_y=-202.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.26, default_y=-202.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=88.11, default_y=-237.81):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='38', width=165.06):
            with Note(default_x=27.51, default_y=-202.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(8.0)
            with Note(default_x=27.51, default_y=-222.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='inverted', default_y=-53.4, relative_y=-10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')