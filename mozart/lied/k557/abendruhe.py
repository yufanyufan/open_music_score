with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Abendruhe')
    with Identification():
        Creator('Wolfgang Amadeus Mozart', type='composer')
        Rights('CPDL   —   Creative Commons Attribution Non Commercial 3.0')
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
            Millimeters(6.4)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1855.79)
            PageWidth(1312.86)
            with PageMargins(type='even'):
                LeftMargin(62.5)
                RightMargin(62.5)
                TopMargin(62.5)
                BottomMargin(125.0)
            with PageMargins(type='odd'):
                LeftMargin(62.5)
                RightMargin(62.5)
                TopMargin(62.5)
                BottomMargin(125.0)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Linux Libertine', font_size='11')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart', default_x=1250.36, default_y=1688.29, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Abendruhe', default_x=656.431, default_y=1793.29, justify='center', valign='top', font_size='22')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('CPDL   —   Creative Commons Attribution Non Commercial 3.0', default_x=656.431, default_y=125.0, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Sopran\nAlt')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Stimme')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Tenor\nBass')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Stimme')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=255.68):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(82.44)
                        RightMargin(0.0)
                    TopSystemDistance(175.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-5)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Langsam', default_x=-36.0, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=80.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=141.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-32.84, default_y=-89.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.\xa0\xa0Wie')
                with Lyric(number='2', default_x=-33.72, default_y=-113.48, relative_y=-30.0):
                    Syllabic('single')
                    Text("2.\xa0\xa0Welch'")
                with Lyric(number='3', default_x=-33.72, default_y=-137.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.\xa0\xa0Wie')
            with Backup():
                Duration(4.0)
            with Note(default_x=141.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='1', width=203.1):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.53)
            with Note(default_x=27.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-89.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
                with Lyric(number='2', default_x=6.22, default_y=-113.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sü')
                with Lyric(number='3', default_x=6.22, default_y=-137.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl')
            with Note(default_x=134.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
                with Lyric(number='2', default_x=6.58, default_y=-113.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßer')
                with Lyric(number='3', default_x=6.58, default_y=-137.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=27.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=134.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=205.8):
            with Note(default_x=31.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-89.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('sind')
                with Lyric(number='2', default_x=6.22, default_y=-113.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
                with Lyric(number='3', default_x=10.16, default_y=-137.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir!')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-47.11, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=137.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-113.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                with Lyric(number='3', default_x=6.58, default_y=-137.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=137.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=215.27):
            with Note(default_x=21.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-89.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
                with Lyric(number='2', default_x=6.22, default_y=-113.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='3', default_x=6.22, default_y=-137.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('at')
            with Note(default_x=122.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-89.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bend')
                with Lyric(number='2', default_y=-113.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='3', default_y=-137.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
                    Extend()
            with Note(default_x=168.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=122.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=225.59):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.89)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-89.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stun')
                with Lyric(number='2', default_y=-113.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schie')
                with Lyric(number='3', default_y=-137.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frei')
            with Note(default_x=68.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=100.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.07, default_y=-89.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('den!')
                with Lyric(number='2', default_x=9.85, default_y=-113.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
                with Lyric(number='3', default_x=9.82, default_y=-137.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('er,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=100.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='5', width=338.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.29)
                        RightMargin(0.0)
                    SystemDistance(96.05)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.63, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Na')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-88.63)
            with Note(default_x=192.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl')
                with Lyric(number='2', default_x=9.71, default_y=-119.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('tur,')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ginnt')
            with Note(default_x=264.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=192.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=264.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=197.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.63, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=26.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.49, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem,')
                with Lyric(number='2', default_x=6.22, default_y=-119.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
                with Lyric(number='3', default_x=8.73, default_y=-143.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text("ew'")
            with Note(default_x=139.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('nem')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Backup():
                Duration(12.0)
            with Note(default_x=27.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=83.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=210.49):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
                    Extend()
                with Lyric(number='2', default_x=1.76, default_y=-119.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text("heil'")
                with Lyric(number='3', default_y=-143.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ster')
            with Note(default_x=79.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=143.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('emp')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Backup():
                Duration(12.0)
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=79.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=143.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='8', width=188.96):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-96.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fun')
                with Lyric(number='2', default_y=-119.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
                with Lyric(number='3', default_y=-143.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fei')
            with Note(default_x=47.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=80.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.07, default_y=-96.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('den!')
                with Lyric(number='2', default_x=10.07, default_y=-119.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('den!')
                with Lyric(number='3', default_x=9.6, default_y=-143.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('er.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='9', width=245.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.42, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=25.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wer')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=98.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wel')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stil')
            with Note(default_x=171.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-96.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
                with Lyric(number='2', default_x=6.58, default_y=-119.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
                with Lyric(number='3', default_x=6.58, default_y=-143.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
            with Backup():
                Duration(12.0)
            with Note(default_x=25.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.28, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=316.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.29)
                        RightMargin(0.0)
                    SystemDistance(96.05)
            with Note(default_x=120.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-97.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Won')
                with Lyric(number='2', default_y=-120.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sün')
                with Lyric(number='3', default_y=-144.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=157.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=195.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                with Lyric(number='3', default_x=10.35, default_y=-144.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('bend,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='11', width=186.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.92, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=29.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('füllt')
                with Lyric(number='2', default_x=6.22, default_y=-120.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ganz')
                with Lyric(number='3', default_x=6.22, default_y=-144.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hol')
            with Note(default_x=125.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
                with Lyric(number='3', default_x=6.58, default_y=-144.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Backup():
                Duration(12.0)
            with Note(default_x=29.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=125.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=186.8):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.53)
            with Note(default_x=10.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.76, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brust!')
                    Extend()
                with Lyric(number='2', default_x=0.44, default_y=-120.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('füllt,')
                    Extend()
                with Lyric(number='3', default_x=0.88, default_y=-144.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zeit,')
                    Extend()
            with Note(default_x=68.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='13', width=277.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.61, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mein')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='3', default_x=6.58, default_y=-144.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freu')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-89.61)
            with Note(default_x=105.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('stimmt')
                with Lyric(number='3', default_x=6.58, default_y=-144.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('dig')
            with Note(default_x=190.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zer')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='3', default_x=6.58, default_y=-144.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=105.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=214.49):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.61, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=31.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-97.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('fließt')
                with Lyric(number='2', default_x=6.22, default_y=-120.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
                with Lyric(number='3', default_x=6.22, default_y=-144.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=143.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-97.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-120.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('bend')
                with Lyric(number='3', default_x=6.58, default_y=-144.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=143.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=263.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.29)
                        RightMargin(0.0)
                    SystemDistance(96.05)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.28)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-93.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rei')
                with Lyric(number='2', default_x=6.22, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh')
                with Lyric(number='3', default_x=6.22, default_y=-140.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lied')
            with Note(default_x=207.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ner')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=207.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=144.49):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.28, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=32.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.93, default_y=-93.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust,')
                with Lyric(number='2', default_x=9.92, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild,')
                with Lyric(number='3', default_x=9.57, default_y=-140.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('weiht,')
            with Backup():
                Duration(12.0)
            with Note(default_x=32.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='17', width=261.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.86, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=22.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freu')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-85.86)
            with Note(default_x=101.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('stimmt')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('dig')
            with Note(default_x=181.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zer')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=101.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=197.26):
            with Note(default_x=31.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-93.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('fließt')
                with Lyric(number='2', default_x=6.22, default_y=-117.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
                with Lyric(number='3', default_x=6.22, default_y=-140.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.36, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=132.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('bend')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=132.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=179.87):
            with Note(default_x=24.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-93.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rei')
                with Lyric(number='2', default_x=6.22, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh')
                with Lyric(number='3', default_x=6.22, default_y=-140.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lied')
            with Note(default_x=119.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-93.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ner')
                with Lyric(number='2', default_x=6.58, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-140.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Backup():
                Duration(12.0)
            with Note(default_x=24.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=131.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=134.77):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=32.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=9.71, default_y=-93.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust.')
                with Lyric(number='2', default_x=9.7, default_y=-117.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild.')
                with Lyric(number='3', default_x=9.79, default_y=-140.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('weiht!')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=32.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=255.68):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(195.87)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-5)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=141.43, default_y=-220.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=141.43, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='1', width=203.1):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=27.75, default_y=-220.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=134.81, default_y=-235.87):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=27.75, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=134.81, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=205.8):
            with Note(default_x=31.5, default_y=-235.87):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=137.91, default_y=-235.87):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.5, default_y=-250.87):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=137.91, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=215.27):
            with Note(default_x=21.58, default_y=-235.87):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=122.26, default_y=-215.87):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=21.58, default_y=-260.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=122.26, default_y=-260.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=225.59):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=13.8, default_y=-220.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=100.83, default_y=-220.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.83, default_y=-255.87):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='5', width=338.66):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(211.29)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=120.38, default_y=-251.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=192.6, default_y=-251.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=264.83, default_y=-251.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-271.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=192.6, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=264.83, default_y=-271.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=197.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=27.05, default_y=-251.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.48, default_y=-231.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.92, default_y=-226.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=26.69, default_y=-276.29):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=139.92, default_y=-271.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=210.49):
            with Note(default_x=13.8, default_y=-231.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=143.98, default_y=-236.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=143.98, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=188.96):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.53)
            with Note(default_x=13.8, default_y=-236.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.18, default_y=-241.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=80.55, default_y=-241.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-251.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.55, default_y=-286.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='9', width=245.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=25.47, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.28, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.1, default_y=-266.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=25.47, default_y=-286.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.28, default_y=-286.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.1, default_y=-286.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=316.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(194.19)
            with Note(default_x=120.38, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=195.11, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.11, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='11', width=186.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=29.07, default_y=-234.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=125.35, default_y=-234.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=29.07, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=125.35, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=186.8):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.53)
            with Note(default_x=10.36, default_y=-234.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=10.36, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
        with Measure(number='13', width=277.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.36, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.11, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.36)
            with Note(default_x=105.91, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.71, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.11, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=105.91, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.71, default_y=-269.19):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=214.49):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.36, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=31.06, default_y=-244.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=143.09, default_y=-229.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.06, default_y=-264.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=143.09, default_y=-274.19):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=263.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(213.78)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.53)
            with Note(default_x=120.38, default_y=-253.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=207.45, default_y=-253.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=120.38, default_y=-288.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=207.45, default_y=-288.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=144.49):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.53, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=32.34, default_y=-253.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=32.34, default_y=-273.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='17', width=261.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.36, relative_y=-40.0):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=22.43, default_y=-258.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.36)
            with Note(default_x=101.73, default_y=-258.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=181.03, default_y=-258.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.43, default_y=-283.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.73, default_y=-283.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.03, default_y=-283.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=197.26):
            with Note(default_x=31.06, default_y=-253.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.86, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=132.49, default_y=-238.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=31.06, default_y=-288.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=132.49, default_y=-293.78):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=179.87):
            with Note(default_x=24.44, default_y=-238.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=119.24, default_y=-243.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=24.44, default_y=-288.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=119.24, default_y=-288.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=134.77):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=32.34, default_y=-238.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=32.15, relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=32.34, default_y=-273.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')