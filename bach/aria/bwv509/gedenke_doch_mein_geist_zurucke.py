with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Aria')
    with Identification():
        Creator('by Unknown BWV 509', type='composer')
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
        CreditWords('Aria', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Gedenke doch, mein Geist, zurücke', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('by Unknown\n', default_x=1134.19, default_y=1486.67, justify='right', valign='bottom', font_size='12')
        CreditWords('BWV 509\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Sopran', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Sopran')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Cembalo', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Cembalo')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(7)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=326.94):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(210.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.96, relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Sound(tempo=98.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=248.27):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=239.57):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Offset(-2.0)
                Sound(tempo=97.9)
        with Measure(number='4', width=241.72):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=97.6)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('45')
                with DirectionType():
                    Words('.6', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=91.2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=184.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.4', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-14.0)
                Sound(tempo=96.8)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('47')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-12.0)
                Sound(tempo=95.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('46')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-10.0)
                Sound(tempo=93.7)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('44')
                Offset(-6.0)
                Sound(tempo=88.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Offset(-6.0)
                Sound(tempo=98.0)
        with Measure(number='5', width=326.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=100.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
            with Note(default_x=152.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke')
            with Note(default_x=212.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.74, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch,')
            with Note(default_x=265.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                    Extend()
            with Note(default_x=298.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=247.45):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist,')
                    Extend()
            with Note(default_x=49.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=76.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zu')
            with Note(default_x=104.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('rük')
            with Note(default_x=185.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke')
            with Note(default_x=213.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ans')
        with Measure(number='7', width=241.94):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Grab')
                    Extend()
            with Note(default_x=42.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=71.02, default_y=-25.0):
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
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=99.11, default_y=-30.0):
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
            with Note(default_x=127.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
                    Extend()
            with Note(default_x=155.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=184.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=212.25, default_y=-15.0):
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
        with Measure(number='8', width=241.09):
            with Note(default_x=10.0, default_y=-15.0):
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
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glok')
            with Note(default_x=38.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ken')
            with Note(default_x=96.35, default_y=-5.0):
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
            with Note(default_x=124.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Ornaments():
                        Mordent()
                with Lyric(number='1', default_x=9.2, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('schlag,')
        with Measure(number='9', width=317.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=264.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='10', width=252.87):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('man')
                    Extend()
            with Note(default_x=65.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=140.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=195.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('zur')
                    Extend()
            with Note(default_x=223.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=238.28):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ruh')
                    Extend()
            with Note(default_x=36.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=89.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=116.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('glei')
            with Note(default_x=169.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.81, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,')
            with Note(default_x=203.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
        with Measure(number='12', width=248.09):
            with Note(default_x=14.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=71.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=99.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=128.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('klüg')
            with Note(default_x=185.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=213.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
        with Measure(number='13', width=414.76):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=111.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ster')
            with Note(default_x=149.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=186.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                    Extend()
            with Note(default_x=224.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=262.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.06, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('mag.')
        with Measure(number='14', width=337.56):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='15', width=304.17):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=97.9)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('45')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=91.7)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=229.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schreib')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.7', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-14.0)
                Sound(tempo=97.4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.1', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-12.0)
                Sound(tempo=96.2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('47')
                with DirectionType():
                    Words('.2', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-10.0)
                Sound(tempo=94.4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('44')
                Offset(-6.0)
                Sound(tempo=88.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Offset(-6.0)
                Sound(tempo=98.0)
        with Measure(number='16', width=388.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=108.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=177.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
                    Extend()
            with Note(default_x=212.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=247.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wort')
            with Note(default_x=316.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
        with Measure(number='17', width=346.28):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
                    Extend()
            with Note(default_x=50.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=90.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=130.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.91, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brust,')
            with Note(default_x=250.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=290.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=97.9)
            with Note(default_x=319.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=322.14):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=97.8)
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.7', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=97.4)
            with Note(default_x=50.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=96.7)
            with Note(default_x=87.6, default_y=-25.0):
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
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke,')
                    Extend()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('47')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=95.7)
            with Note(default_x=124.49, default_y=-30.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('47')
                with DirectionType():
                    Words('.2', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=94.4)
            with Note(default_x=161.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                    Extend()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('46')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=92.7)
            with Note(default_x=209.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('45')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=90.6)
            with Note(default_x=246.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('44')
                Sound(tempo=88.1)
            with Note(default_x=283.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=481.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('42')
                with DirectionType():
                    Words('.5', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=85.1)
            with Note(default_x=111.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ster')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('40')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=81.6)
            with Note(default_x=157.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('38')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=77.6)
            with Note(default_x=203.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                    Extend()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('36')
                with DirectionType():
                    Words('.5', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=73.1)
            with Note(default_x=249.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('34')
                Sound(tempo=68.0)
            with Note(default_x=295.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.28, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('musst.')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Offset(-6.0)
                Sound(tempo=98.0)
        with Measure(number='20', width=306.27):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('49')
                Offset(-14.0)
                Sound(tempo=97.9)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-12.0)
                Sound(tempo=97.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('48')
                with DirectionType():
                    Words('.4', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-10.0)
                Sound(tempo=96.8)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('47')
                with DirectionType():
                    Words('.7', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-8.0)
                Sound(tempo=95.4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('46')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-6.0)
                Sound(tempo=93.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('45')
                with DirectionType():
                    Words('.5', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-4.0)
                Sound(tempo=90.9)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('43')
                with DirectionType():
                    Words('.8', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-2.0)
                Sound(tempo=87.6)
        with Measure(number='21', width=268.41):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('41')
                with DirectionType():
                    Words('.7', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=83.5)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('39')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-14.0)
                Sound(tempo=78.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('36')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-12.0)
                Sound(tempo=72.6)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('32')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-10.0)
                Sound(tempo=65.8)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('half')
                        PerMinute('29')
                Offset(-8.0)
                Sound(tempo=58.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=326.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(68.34)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
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
            with Note(default_x=126.78, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=227.79, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Staff(1)
            with Note(default_x=173.84, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=224.34, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=274.84, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=123.34, default_y=-228.34):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=148.59, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.84, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.09, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=224.34, default_y=-223.34):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=249.59, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.84, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.09, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='2', width=248.27):
            with Note(default_x=13.95, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.95, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.39, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.84, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=195.73, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=26.17, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=136.89, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-218.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=54.55, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=82.0, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.44, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=136.89, default_y=-213.34):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=164.33, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.78, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.22, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=239.57):
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=66.99, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.49, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=127.93, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.92, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=213.42, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Staff(1)
            with Note(default_x=123.98, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.48, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=180.97, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-218.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.5, default_y=-193.34):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.99, default_y=-203.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.49, default_y=-213.34):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.98, default_y=-223.34):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=152.48, default_y=-233.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.97, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.47, default_y=-233.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=241.72):
            with Note(default_x=13.95, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=69.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=132.83, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=188.45, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=77.49, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=77.49, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=101.07, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=101.07, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=128.88, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=184.5, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-228.34):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.81, default_y=-238.34):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.62, default_y=-248.34):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.07, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=128.88, default_y=-228.34):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.69, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.5, default_y=-243.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.31, default_y=-208.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=326.01):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.91)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=104.33, default_y=-156.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=156.78, default_y=-166.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=216.25, default_y=-151.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=100.38, default_y=-171.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.83, default_y=-176.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=212.8, default_y=-171.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=100.38, default_y=-246.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.6, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=152.83, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.06, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=212.8, default_y=-241.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=239.03, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=265.25, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.19, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=247.45):
            with Note(default_x=13.44, default_y=-166.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=134.85, default_y=-161.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-176.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=131.4, default_y=-171.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-236.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.73, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=76.96, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=104.18, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=131.4, default_y=-251.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=158.63, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.85, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.07, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='7', width=241.94):
            with Note(default_x=13.95, default_y=-156.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=74.97, default_y=-166.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=131.15, default_y=-151.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=188.11, default_y=-136.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-176.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=127.2, default_y=-161.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=184.16, default_y=-151.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-246.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.93, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.02, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.11, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=127.2, default_y=-251.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.29, default_y=-216.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.16, default_y=-241.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.25, default_y=-216.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=241.09):
            with Note(default_x=13.95, default_y=-146.91):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=71.68, default_y=-141.91):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.3, default_y=-136.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.93, default_y=-141.91):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=186.19, default_y=-151.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-156.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=96.35, default_y=-161.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=124.98, default_y=-166.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-236.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.63, default_y=-241.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.73, default_y=-246.91):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.35, default_y=-251.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=124.98, default_y=-266.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.61, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.24, default_y=-256.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.86, default_y=-231.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=317.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=112.17, default_y=-155.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=166.55, default_y=-165.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=217.57, default_y=-170.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=268.58, default_y=-150.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=108.22, default_y=-175.05):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=229.78, default_y=-170.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=264.63, default_y=-160.05):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=108.22, default_y=-245.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=133.73, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.6, default_y=-235.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.11, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=213.62, default_y=-240.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=239.13, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.63, default_y=-250.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.14, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='10', width=252.87):
            with Note(default_x=13.44, default_y=-150.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=144.36, default_y=-150.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=199.79, default_y=-135.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.87, default_y=-155.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=65.43, default_y=-165.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=156.58, default_y=-150.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-245.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.71, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.43, default_y=-265.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.31, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.41, default_y=-240.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=168.13, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.84, default_y=-265.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.56, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='11', width=238.28):
            with Note(default_x=13.95, default_y=-135.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=67.08, default_y=-140.05):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=119.7, default_y=-135.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-165.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.56, default_y=-160.05):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=63.13, default_y=-155.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=116.25, default_y=-160.05):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=169.38, default_y=-150.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-235.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.56, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=63.13, default_y=-265.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.69, default_y=-230.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.25, default_y=-250.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.82, default_y=-215.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.38, default_y=-240.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.91, default_y=-215.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=248.09):
            with Note(default_x=17.66, default_y=-145.05):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=132.44, default_y=-135.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=189.38, default_y=-140.05):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=217.85, default_y=-145.05):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=30.38, default_y=-145.05):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=71.16, default_y=-165.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=128.49, default_y=-145.05):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=185.43, default_y=-155.05):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=213.9, default_y=-165.05):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.22, default_y=-235.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.69, default_y=-215.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.16, default_y=-225.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.63, default_y=-215.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=128.49, default_y=-235.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.96, default_y=-225.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.43, default_y=-245.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.9, default_y=-235.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=414.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.53)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=115.53, default_y=-130.53):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=190.93, default_y=-145.53):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=190.93, default_y=-135.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=266.32, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=341.72, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=379.42, default_y=-145.53):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.58, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=111.58, default_y=-140.53):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=186.98, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.68, default_y=-160.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=262.37, default_y=-165.53):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=337.77, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.58, default_y=-255.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.28, default_y=-245.53):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.98, default_y=-235.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.68, default_y=-270.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=262.37, default_y=-255.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=300.07, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=337.77, default_y=-245.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.47, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=337.56):
            with Note(default_x=13.44, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=175.04, default_y=-160.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=219.09, default_y=-150.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=259.37, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=299.64, default_y=-125.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-150.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=90.55, default_y=-165.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=187.26, default_y=-160.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=255.42, default_y=-150.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-240.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.27, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=90.55, default_y=-235.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.82, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
            with Note(default_x=171.1, default_y=-230.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.14, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.42, default_y=-240.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.69, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=304.17):
            with Note(default_x=13.95, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=13.95, default_y=-130.53):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=87.09, default_y=-145.53):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=87.09, default_y=-135.53):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=159.73, default_y=-140.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=83.14, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.71, default_y=-160.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.28, default_y=-165.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=229.43, default_y=-155.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with FiguredBass():
                with Figure():
                    FigureNumber('6')
                with Figure():
                    FigureNumber('4')
            with Note(default_x=10.0, default_y=-235.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.57, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with FiguredBass():
                with Figure():
                    FigureNumber('5')
                with Figure():
                    Prefix('natural')
            with Note(default_x=83.14, default_y=-270.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.71, default_y=-235.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.28, default_y=-255.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=192.85, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.43, default_y=-245.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.0, default_y=-220.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='16', width=388.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.49)
                with StaffLayout(number=2):
                    StaffDistance(91.67)
            with Note(default_x=126.83, default_y=-164.49):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=126.83, default_y=-139.49):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=251.3, default_y=-139.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=320.86, default_y=-134.49):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=108.22, default_y=-144.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=177.79, default_y=-154.49):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=247.35, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=316.91, default_y=-149.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=351.69, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=108.22, default_y=-261.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.0, default_y=-246.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.79, default_y=-251.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.57, default_y=-246.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=247.35, default_y=-256.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=282.13, default_y=-246.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.91, default_y=-266.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=351.69, default_y=-241.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='17', width=346.28):
            with Note(default_x=13.95, default_y=-134.49):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-144.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.16, default_y=-149.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=174.38, default_y=-149.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=254.59, default_y=-139.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-154.49):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=90.21, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.32, default_y=-164.49):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.43, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=242.72, default_y=-164.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=250.64, default_y=-159.49):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-251.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.11, default_y=-261.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.21, default_y=-256.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.32, default_y=-291.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=170.43, default_y=-276.16):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=210.53, default_y=-266.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=250.64, default_y=-291.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.75, default_y=-266.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='18', width=322.14):
            with Note(default_x=17.24, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=165.34, default_y=-169.49):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=213.8, default_y=-164.49):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=250.7, default_y=-159.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-169.49):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=87.6, default_y=-179.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=177.56, default_y=-169.49):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=246.75, default_y=-169.49):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=283.64, default_y=-179.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-286.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.7, default_y=-266.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.6, default_y=-276.16):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.49, default_y=-266.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=161.39, default_y=-286.16):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=209.85, default_y=-261.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.75, default_y=-276.16):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.64, default_y=-261.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='19', width=481.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(78.38)
            with Note(default_x=115.53, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=207.69, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=299.85, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=392.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.58, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=203.74, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=249.82, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=295.9, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=388.06, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.58, default_y=-253.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.66, default_y=-228.38):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.74, default_y=-233.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.82, default_y=-223.38):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=295.9, default_y=-238.38):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=341.98, default_y=-208.38):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=388.06, default_y=-228.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=434.14, default_y=-208.38):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='20', width=306.27):
            with Note(default_x=17.75, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=90.47, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=163.18, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=235.9, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter', size='cue')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=86.52, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=159.23, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter', size='cue')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=268.31, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-223.38):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.16, default_y=-213.38):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.52, default_y=-223.38):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.87, default_y=-233.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=159.23, default_y=-243.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.59, default_y=-253.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.95, default_y=-238.38):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.31, default_y=-248.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='21', width=268.41):
            with Note(default_x=13.44, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
            with Note(default_x=173.32, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half', size='cue')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.87, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=93.89, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.86, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth', size='cue')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.88, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half', size='cue')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=89.94, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.77, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth', size='cue')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=10.0, default_y=-258.38):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.97, default_y=-268.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.94, default_y=-253.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.91, default_y=-243.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.52, default_y=-273.38):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')