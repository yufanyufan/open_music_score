with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Nei campi e nelle selve')
    with Identification():
        Creator('Ludvig van Beethoven', type='composer')
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
        CreditType('title')
        CreditWords('Nei campi e nelle selve', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(Zweite Komposition)', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludvig van Beethoven', default_x=1134.19, default_y=1514.17, justify='right', valign='bottom', font_size='12')
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
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('T\nB')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Tenor/Bass')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=118.47):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.4)
                        RightMargin(0.0)
                    TopSystemDistance(193.7)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, relative_x=-106.46, relative_y=38.5):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('(Allegro)', relative_x=-33.0, relative_y=64.0, font_weight='bold', font_size='12')
            with Note(default_x=80.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('Nei')
            with Backup():
                Duration(4.0)
            with Note(default_x=80.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='1', width=181.04):
            with Note(default_x=23.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('cam')
            with Note(default_x=64.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('pi e')
            with Note(default_x=102.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('nel')
            with Note(default_x=140.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('le')
            with Backup():
                Duration(16.0)
            with Note(default_x=23.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=102.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=140.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='2', width=149.43):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=3.92, default_y=-70.85, relative_x=3.92, relative_y=-55.0):
                    Syllabic('begin')
                    Text('sel')
            with Note(default_x=56.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=81.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('ve')
            with Note(default_x=114.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('se')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=56.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=81.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=114.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='3', width=155.87):
            with Note(default_x=18.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('gui')
            with Note(default_x=52.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('vo')
            with Note(default_x=86.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('già')
            with Note(default_x=120.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('le')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=52.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=86.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=142.56):
            with Note(default_x=18.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('bel')
            with Note(default_x=47.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=11.01, default_y=-70.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('ve,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pas')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=47.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=106.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='5', width=210.88):
            with Note(default_x=14.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('ce')
            with Note(default_x=63.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('vo il')
            with Note(default_x=112.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('greg')
            with Note(default_x=160.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('ge an')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=112.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=160.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='6', width=85.85):
            with Note(default_x=19.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('cor')
            with Note(default_x=51.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=-2.08, default_y=-70.85, relative_x=-2.08, relative_y=-55.0):
                    Syllabic('begin')
                    Text('li')
            with Backup():
                Duration(16.0)
            with Note(default_x=19.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='7', width=243.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=129.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('end')
                    Text('ro')
            with Note(default_x=157.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=199.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('middle')
                    Text('sto')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=129.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=157.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=130.24):
            with Note(default_x=16.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('middle')
                    Text('rel')
            with Note(default_x=47.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=11.0, default_y=-75.45, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('lo,')
            with Note(default_x=78.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=-2.08, default_y=-75.45, relative_x=-2.08, relative_y=-55.0):
                    Syllabic('begin')
                    Text('li')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=47.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=204.04):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=87.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('end')
                    Text('ro')
            with Note(default_x=115.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('begin')
                    Text('cac')
            with Note(default_x=158.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('middle')
                    Text('cia')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=87.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=115.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=158.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='10', width=82.4):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.68, default_y=-75.45, relative_x=2.64, relative_y=-55.0):
                    Syllabic('end')
                    Text('tor.')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('up')
        with Measure(number='11', width=258.18):
            with Attributes():
                with Key():
                    Fifths(-3)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', relative_x=-18.0, relative_y=65.5, font_weight='bold', font_size='12')
            with Note(default_x=43.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('begin')
                    Text('O')
            with Note(default_x=86.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('end')
                    Text('ra')
            with Note(default_x=114.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=150.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=203.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('single')
                    Text('più')
            with Backup():
                Duration(16.0)
            with Note(default_x=43.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=86.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=114.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=150.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=152.82):
            with Note(default_x=14.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('begin')
                    Text('quel')
            with Note(default_x=48.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=11.0, default_y=-75.45, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('lo:')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=115.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.45, relative_y=-55.0):
                    Syllabic('begin')
                    Text('Per')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=115.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=267.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('end')
                    Text('dei')
            with Note(default_x=144.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=172.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('begin')
                    Text('li')
            with Note(default_x=218.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('middle')
                    Text('ber')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=144.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=172.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=195.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=166.21):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.94, default_y=-61.4, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('tà.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('E')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=127.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='15', width=240.22):
            with Note(default_x=23.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('quel')
            with Note(default_x=82.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('chè')
            with Note(default_x=121.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('begin')
                    Text('peg')
            with Note(default_x=170.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=11.05, default_y=-61.4, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('gio,')
            with Note(default_x=205.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('oh')
            with Backup():
                Duration(16.0)
            with Note(default_x=23.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=82.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=121.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=205.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='16', width=125.19):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('begin')
                    Text('Di')
            with Note(default_x=46.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=12.59, default_y=-61.4, relative_x=3.01, relative_y=-55.0):
                    Syllabic('end')
                    Text('o!')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=46.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='17', width=272.46):
            with Note(default_x=44.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-61.4, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('begin')
                    Text('Co')
            with Note(default_x=95.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-61.4, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=134.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-61.4, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('single')
                    Text('se il')
            with Note(default_x=162.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-61.4, relative_y=-55.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=221.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Lyric(number='1', default_x=3.92, default_y=-61.4, relative_x=3.92, relative_y=-55.0):
                    Syllabic('begin')
                    Text('tor')
            with Note(default_x=247.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(16.0)
            with Note(default_x=32.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=83.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=122.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=162.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=221.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=247.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='18', width=276.52):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=98.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=136.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('to')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=136.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='19', width=257.72):
            with Note(default_x=44.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-60.85, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('begin')
                    Text('col')
            with Note(default_x=88.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-60.85, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('end')
                    Text('pa')
            with Note(default_x=128.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=-17.16, default_y=-60.85, relative_x=-11.87, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=155.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('sia')
            with Note(default_x=206.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('di')
            with Note(default_x=232.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(16.0)
            with Note(default_x=32.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=76.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=116.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=155.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=206.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=232.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='20', width=208.22):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=55.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.98, default_y=-60.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('i,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('mo')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=55.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=156.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='21', width=199.02):
            with Note(default_x=22.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('stra')
            with Note(default_x=63.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('re al')
            with Note(default_x=101.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=149.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('la')
            with Backup():
                Duration(16.0)
            with Note(default_x=22.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=101.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=129.81):
            with Note(default_x=24.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=63.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-60.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('to')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='23', width=318.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(137.39)
            with Note(default_x=98.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('Clo')
            with Note(default_x=145.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('ri')
            with Note(default_x=186.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=223.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('vuol')
            with Note(default_x=270.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pie')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=186.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('natural')
                Stem('up')
            with Note(default_x=223.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=270.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='24', width=141.71):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.14, default_y=-75.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('tà,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='25', width=220.46):
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('co')
            with Note(default_x=60.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=93.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('se il')
            with Note(default_x=129.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=185.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('tor')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=60.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=93.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=129.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=185.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='26', width=189.16):
            with Note(default_x=24.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=64.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('to')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='27', width=201.96):
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('col')
            with Note(default_x=56.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('pa')
            with Note(default_x=85.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=115.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('sia')
            with Note(default_x=167.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-75.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('di')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=85.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=115.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=167.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='28', width=228.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(137.39)
            with Note(default_x=98.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=130.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.98, default_y=-70.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('i,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('mo')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=130.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=192.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='29', width=184.23):
            with Note(default_x=21.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('stra')
            with Note(default_x=67.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('real')
            with Note(default_x=103.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=149.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('la')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=67.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=103.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=149.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='30', width=136.64):
            with Note(default_x=24.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=76.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('to')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=76.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='31', width=233.41):
            with Note(default_x=20.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('Clo')
            with Note(default_x=65.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('end')
                    Text('ri')
            with Note(default_x=104.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=142.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('vuol')
            with Note(default_x=187.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pie')
            with Backup():
                Duration(16.0)
            with Note(default_x=20.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=65.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=104.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Accidental('flat')
                Stem('up')
            with Note(default_x=142.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=187.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
        with Measure(number='32', width=111.93):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.14, default_y=-70.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('tà,')
            with Note(default_x=63.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
        with Measure(number='33', width=176.15):
            with Note(default_x=19.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=11.07, default_y=-70.85, relative_x=2.26, relative_y=-55.0):
                    Syllabic('single')
                    Text('vuol,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-70.85, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pie')
            with Backup():
                Duration(16.0)
            with Note(default_x=19.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=135.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='34', width=442.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(137.39)
            with Note(default_x=98.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=11.14, default_y=-59.8, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('tà,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=355.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-59.8, relative_y=-55.0):
                    Syllabic('single')
                    Text('non')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=355.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='35', width=341.82):
            with Note(default_x=24.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.59, default_y=-59.8, relative_y=-55.0):
                    Syllabic('single')
                    Text('vuol')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=182.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=5.42, default_y=-59.8, relative_x=5.42, relative_y=-55.0):
                    Syllabic('begin')
                    Text('pie')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=182.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
        with Measure(number='36', width=287.41):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.94, default_y=-59.8, relative_x=2.26, relative_y=-55.0):
                    Syllabic('end')
                    Text('tà.')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C.', relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=118.47):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(171.3)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=80.83, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(4.0)
            with Note(default_x=80.83, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='1', width=181.04):
            with Note(default_x=23.4, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=64.1, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=102.55, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=140.99, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=23.4, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.1, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=102.55, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=140.99, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='2', width=149.43):
            with Note(default_x=15.8, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.52, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=114.68, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.52, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=114.68, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='3', width=155.87):
            with Note(default_x=18.8, default_y=-221.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=52.67, default_y=-221.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=86.53, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.4, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.8, default_y=-186.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=52.67, default_y=-186.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=86.53, default_y=-196.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.4, default_y=-196.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=142.56):
            with Note(default_x=18.6, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=47.79, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.16, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.6, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=47.79, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=106.16, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='5', width=210.88):
            with Note(default_x=14.8, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=63.42, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=112.04, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=160.66, default_y=-216.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.8, default_y=-206.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.42, default_y=-206.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=112.04, default_y=-206.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=160.66, default_y=-206.3):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='6', width=85.85):
            with Note(default_x=19.2, default_y=-236.3):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.72, default_y=-221.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=19.2, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.72, default_y=-201.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='7', width=243.61):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(176.5)
            with Note(default_x=59.77, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.99, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=129.79, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=157.59, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=199.8, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.99, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=129.79, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=157.59, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.8, default_y=-201.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=130.24):
            with Note(default_x=16.8, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=47.87, default_y=-216.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.93, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.8, default_y=-211.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=47.87, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.93, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=204.04):
            with Note(default_x=15.8, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.48, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=87.28, default_y=-226.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=115.08, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=158.76, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.48, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=87.28, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=115.08, default_y=-186.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=158.76, default_y=-186.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='10', width=82.4):
            with Note(default_x=15.8, default_y=-241.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('half')
                Stem('up')
        with Measure(number='11', width=258.18):
            with Attributes():
                with Key():
                    Fifths(-3)
            with Note(default_x=43.8, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=86.24, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=114.04, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=150.34, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=203.39, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=43.8, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=86.24, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=114.04, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=150.34, default_y=-211.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=203.39, default_y=-201.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='12', width=152.82):
            with Note(default_x=14.6, default_y=-221.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=48.27, default_y=-241.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=115.62, default_y=-241.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.6, default_y=-211.5):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=48.27, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=115.62, default_y=-206.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=267.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(156.85)
            with Note(default_x=98.78, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=144.36, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=172.16, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=218.89, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=144.36, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=172.16, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=218.89, default_y=-171.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.25, default_y=-176.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=166.21):
            with Note(default_x=15.8, default_y=-201.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.41, default_y=-201.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-176.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.0, default_y=-181.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=127.41, default_y=-191.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
        with Measure(number='15', width=240.22):
            with Note(default_x=23.6, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=82.43, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=121.96, default_y=-196.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=170.21, default_y=-201.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=205.82, default_y=-201.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=23.6, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=82.43, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=121.96, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.21, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=205.82, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='16', width=125.19):
            with Note(default_x=17.23, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=46.78, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=46.78, default_y=-186.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='17', width=272.46):
            with Note(default_x=32.56, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=83.35, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=122.75, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=162.14, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=221.03, default_y=-206.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=32.56, default_y=-196.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=83.35, default_y=-196.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=122.75, default_y=-196.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=162.14, default_y=-196.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=221.03, default_y=-181.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='18', width=276.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(151.9)
            with Note(default_x=98.78, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=136.86, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=174.95, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('col')
            with Note(default_x=213.03, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('pa')
            with Note(default_x=242.13, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('non')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=136.86, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='19', width=257.72):
            with Note(default_x=32.96, default_y=-201.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.91, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('sia,')
            with Note(default_x=116.13, default_y=-201.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=155.53, default_y=-201.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('sia')
            with Note(default_x=206.28, default_y=-201.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('di')
            with Backup():
                Duration(16.0)
            with Note(default_x=32.96, default_y=-191.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
            with Note(default_x=116.13, default_y=-191.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=155.53, default_y=-191.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=206.28, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='20', width=208.22):
            with Note(default_x=15.8, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=55.56, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=8.73, default_y=-60.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('i,')
            with Note(default_x=80.84, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=116.74, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stra')
            with Note(default_x=156.5, default_y=-196.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('re')
            with Note(default_x=181.77, default_y=-211.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('al')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=55.56, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=156.5, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='21', width=199.02):
            with Note(default_x=22.44, default_y=-221.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
            with Note(default_x=63.54, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('al')
            with Note(default_x=101.84, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=149.63, default_y=-186.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('la')
            with Backup():
                Duration(16.0)
            with Note(default_x=22.44, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.54, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=101.84, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=149.63, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='22', width=129.81):
            with Note(default_x=36.08, default_y=-181.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-5.28, default_y=-60.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=63.61, default_y=-216.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('to')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.22, default_y=-176.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=63.61, default_y=-181.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='23', width=318.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(169.05)
            with Note(default_x=98.78, default_y=-234.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=145.12, default_y=-234.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
            with Note(default_x=186.22, default_y=-234.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=223.72, default_y=-229.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=270.06, default_y=-229.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-199.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.12, default_y=-199.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=186.22, default_y=-199.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
            with Note(default_x=223.72, default_y=-204.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=270.06, default_y=-199.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='24', width=141.71):
            with Note(default_x=12.0, default_y=-249.05):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-204.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.39, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.59, default_y=20.45, relative_y=31.0):
                    Syllabic('begin')
                    Text('co')
            with Note(default_x=92.26, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=15.49, default_y=20.45, relative_x=6.76, relative_y=31.0):
                    Syllabic('end')
                    Text('me,')
        with Measure(number='25', width=220.46):
            with Note(default_x=14.0, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=60.08, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=93.18, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=129.68, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=185.86, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=60.08, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=93.18, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=129.68, default_y=-209.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=185.86, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='26', width=189.16):
            with Note(default_x=24.2, default_y=-234.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=64.65, default_y=-234.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.2, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=64.65, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=105.09, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.59, default_y=20.45, relative_x=3.01, relative_y=32.5):
                    Syllabic('begin')
                    Text('col')
            with Note(default_x=145.54, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=14.16, default_y=20.45, relative_x=5.26, relative_y=34.0):
                    Syllabic('end')
                    Text('pa,')
        with Measure(number='27', width=201.96):
            with Note(default_x=14.0, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=56.42, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=85.52, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=115.82, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=167.56, default_y=-239.05):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.42, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=85.52, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=115.82, default_y=-209.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=167.56, default_y=-214.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='28', width=228.93):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(179.05)
            with Note(default_x=98.78, default_y=-244.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=130.16, default_y=-244.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.93, default_y=-234.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.78, default_y=-224.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=130.16, default_y=-224.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=192.93, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='29', width=184.23):
            with Note(default_x=21.0, default_y=-234.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=67.67, default_y=-234.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=103.17, default_y=-234.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=149.83, default_y=-234.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.0, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=67.67, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
            with Note(default_x=103.17, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=149.83, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
        with Measure(number='30', width=136.64):
            with Note(default_x=24.2, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=76.33, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.2, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.07, default_y=-194.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=76.33, default_y=-194.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='31', width=233.41):
            with Note(default_x=20.6, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=65.29, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
            with Note(default_x=104.93, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=142.43, default_y=-224.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=187.12, default_y=-224.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=20.6, default_y=-194.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=65.29, default_y=-194.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=104.93, default_y=-194.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('up')
            with Note(default_x=142.43, default_y=-199.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=187.12, default_y=-204.05):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
        with Measure(number='32', width=111.93):
            with Note(default_x=15.8, default_y=-244.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.06, default_y=-219.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-199.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.06, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
        with Measure(number='33', width=176.15):
            with Note(default_x=19.67, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=58.39, default_y=-229.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=97.11, default_y=-224.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Backup():
                Duration(16.0)
            with Note(default_x=19.67, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=58.39, default_y=-209.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('non')
            with Note(default_x=97.11, default_y=-214.05):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('voul')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
        with Measure(number='34', width=442.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(140.85)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=184.29, default_y=-205.85):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=269.68, default_y=-180.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=355.07, default_y=-180.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=184.29, default_y=-160.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pie')
            with Note(default_x=269.68, default_y=-170.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-55.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('tà,')
            with Note(default_x=355.07, default_y=-170.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('non')
        with Measure(number='35', width=341.82):
            with Note(default_x=24.22, default_y=-190.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=182.22, default_y=-185.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Backup():
                Duration(16.0)
            with Note(default_x=24.22, default_y=-170.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('vuol')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=182.22, default_y=-175.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_y=-55.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pie')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
        with Measure(number='36', width=287.41):
            with Note(default_x=15.8, default_y=-205.85):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-170.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.69, default_y=-55.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('tà.')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')