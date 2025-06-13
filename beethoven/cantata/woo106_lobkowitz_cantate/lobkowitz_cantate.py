with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Lobkowitz-Cantate')
    with Identification():
        Creator('L. van Beethoven ', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/3099636/scores/6075599')
    with Defaults():
        with Scaling():
            Millimeters(5.456)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2176.91)
            PageWidth(1540.03)
            with PageMargins(type='even'):
                LeftMargin(73.3138)
                RightMargin(73.3138)
                TopMargin(73.3138)
                BottomMargin(146.628)
            with PageMargins(type='odd'):
                LeftMargin(73.3138)
                RightMargin(73.3138)
                TopMargin(73.3138)
                BottomMargin(146.628)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Lobkowitz-Cantate', default_x=770.015, default_y=2103.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('L. van Beethoven ', default_x=1466.72, default_y=2003.6, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Solo')
            PartAbbreviation('Solo')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(6)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P2'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P6'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro non troppo', default_x=-41.11, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=120.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=157.65):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='2', width=174.19):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=71.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=137.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='3', width=189.82):
            with Note(default_x=13.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=77.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
                    Extend()
            with Note(default_x=94.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=151.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='4', width=247.37):
            with Note(default_x=24.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=79.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=135.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=162.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
                    Extend()
            with Note(default_x=218.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=167.15):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
                    Extend()
            with Note(default_x=54.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='6', width=228.76):
            with Note(default_x=13.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=66.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=93.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=120.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=173.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=200.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=141.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='8', width=234.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=268.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=361.69):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=222.99):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio assai', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=215.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('E')
            with Note(default_x=302.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.01, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('del,')
        with Measure(number='13', width=197.86):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=58.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=9.01, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('del,')
            with Note(default_x=104.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=127.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('del')
                    Extend()
            with Note(default_x=173.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=275.61):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('han')
            with Note(default_x=44.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('deln,')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=172.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja')
            with Note(default_x=204.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=236.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('del')
        with Measure(number='15', width=250.81):
            with Note(default_x=16.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('han')
            with Note(default_x=43.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('deln,')
            with Note(default_x=141.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=195.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein')
        with Measure(number='16', width=258.45):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=134.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=164.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=194.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ster')
            with Note(default_x=224.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=99.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ruf!')
                    Extend()
            with Note(default_x=157.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=208.8):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=112.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.36, default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dann,')
        with Measure(number='19', width=319.39):
            with Note(default_x=26.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
            with Note(default_x=158.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=198.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('imn')
            with Note(default_x=240.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=280.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('eng')
        with Measure(number='20', width=204.45):
            with Note(default_x=15.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=62.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('hen')
            with Note(default_x=109.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                    Extend()
            with Note(default_x=179.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=254.45):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=42.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.17, default_y=-49.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ste,')
            with Note(default_x=132.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=162.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=192.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ste')
                    Extend()
            with Note(default_x=222.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    SystemDistance(137.5)
            with Note(default_x=98.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lohn,')
                    Extend()
            with Note(default_x=159.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=189.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=231.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=291.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.17, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ste,')
        with Measure(number='23', width=481.58):
            with Note(default_x=30.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=73.62, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.58, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=95.55, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=106.52, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=117.48, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=128.45, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.41, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=150.38, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=161.35, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.31, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=183.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ste')
            with Note(default_x=219.72, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=238.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lohn')
            with Note(default_x=253.08, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=264.04, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=275.01, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=285.97, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=296.94, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=307.91, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=318.87, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=329.84, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=340.8, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=351.77, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
            with Note(default_x=370.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=14.58, relative_y=23.92)
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='24', width=234.87):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tempo primo', default_y=4.92, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=120.0)
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=92.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=179.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='25', width=251.16):
            with Note(default_x=13.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=98.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
                    Extend()
            with Note(default_x=116.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=192.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.04)
                        RightMargin(0.0)
                    SystemDistance(137.5)
            with Note(default_x=98.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=150.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=202.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=227.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=253.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
                    Extend()
            with Note(default_x=279.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=152.33):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
                    Extend()
            with Note(default_x=50.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='28', width=213.95):
            with Note(default_x=13.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=61.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=88.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=112.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=187.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='29', width=130.5):
            with Note(default_x=13.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=50.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=217.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=146.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=153.24):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(52.38)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=227.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=190.55):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=215.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=223.48):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=222.63):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(52.38)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=245.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=174.59):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=157.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=174.19):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=189.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=247.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=167.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=228.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.4)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=184.36, default_y=-115.4):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='8', width=234.94):
            with Note(default_x=15.8, default_y=-120.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=63.48, default_y=-120.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=93.28, default_y=-120.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=123.09, default_y=-115.4):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=170.77, default_y=-115.4):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=200.57, default_y=-115.4):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='9', width=268.15):
            with Note(default_x=15.8, default_y=-120.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.3, default_y=-120.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=361.69):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=222.99):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=197.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=275.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=250.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=258.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=208.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=319.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=204.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=254.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=481.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=234.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=251.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(82.17)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=152.33):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=213.95):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=130.5):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=87.47, default_y=-122.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='30', width=217.46):
            with Note(default_x=15.8, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.97, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=85.95, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=112.93, default_y=-122.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=156.1, default_y=-122.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=183.08, default_y=-122.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='31', width=146.86):
            with Note(default_x=15.8, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=48.16, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Note(default_x=80.53, default_y=-122.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.52, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja!')
            with Note(default_x=112.89, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='32', width=153.24):
            with Note(default_x=16.16, default_y=-127.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=54.38, default_y=-132.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.05, default_y=-137.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.71, default_y=-142.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=118.68, default_y=-137.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=102.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=146.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
                    Extend()
            with Note(default_x=163.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=221.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='34', width=227.52):
            with Note(default_x=24.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=69.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=113.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=141.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
                    Extend()
            with Note(default_x=197.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=190.55):
            with Note(default_x=28.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
                    Extend()
            with Note(default_x=68.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=108.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=156.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='36', width=215.8):
            with Note(default_x=24.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=83.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=122.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=181.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='37', width=223.48):
            with Note(default_x=28.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.41, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=84.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
            with Note(default_x=113.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=189.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='38', width=222.63):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=60.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=88.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=115.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-43.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=188.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=98.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=150.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=245.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=174.59):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=157.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=174.19):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=189.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=247.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=167.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=228.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.25)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=184.36, default_y=-266.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='8', width=234.94):
            with Note(default_x=15.8, default_y=-271.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=63.48, default_y=-271.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=93.28, default_y=-271.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=123.09, default_y=-266.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=170.77, default_y=-266.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=200.57, default_y=-266.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='9', width=268.15):
            with Note(default_x=15.8, default_y=-271.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.3, default_y=-271.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=361.69):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=222.99):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=197.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=275.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=250.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=258.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=208.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=319.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=204.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=254.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=481.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=234.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=251.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(131.56)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=152.33):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=213.95):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=130.5):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=87.47, default_y=-318.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='30', width=217.46):
            with Note(default_x=15.8, default_y=-323.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.97, default_y=-323.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-46.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=85.95, default_y=-323.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=112.93, default_y=-318.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=156.1, default_y=-318.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-46.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=183.08, default_y=-318.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='31', width=146.86):
            with Note(default_x=15.8, default_y=-323.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=48.16, default_y=-323.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Note(default_x=80.53, default_y=-303.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.52, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja!')
            with Note(default_x=112.89, default_y=-313.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='32', width=153.24):
            with Note(default_x=15.8, default_y=-333.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.9, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=85.71, default_y=-333.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-46.9, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=118.68, default_y=-333.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.92)
            with Note(default_x=102.94, default_y=-169.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=146.75, default_y=-169.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Note(default_x=183.88, default_y=-169.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=221.66, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='34', width=227.52):
            with Note(default_x=24.3, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=69.1, default_y=-164.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=113.91, default_y=-164.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=141.91, default_y=-169.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.91, default_y=-164.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
                    Extend()
            with Note(default_x=197.91, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=190.55):
            with Note(default_x=28.19, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
                    Extend()
            with Note(default_x=68.74, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.13, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=156.17, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='36', width=215.8):
            with Note(default_x=24.3, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=83.47, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=122.25, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=181.42, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='37', width=223.48):
            with Note(default_x=28.19, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.41, default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=84.75, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
            with Note(default_x=113.74, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.12, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=189.1, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='38', width=222.63):
            with Note(default_x=15.8, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=60.3, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=88.12, default_y=-159.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=115.94, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.44, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-49.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=188.26, default_y=-154.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.4)
            with Note(default_x=98.78, default_y=-149.4):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=150.0, default_y=-149.4):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=245.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=174.59):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=157.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=174.19):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=189.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=247.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=167.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=228.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.5)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=184.36, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='8', width=234.94):
            with Note(default_x=15.8, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=63.48, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=93.28, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=123.09, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=170.77, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=200.57, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='9', width=268.15):
            with Note(default_x=15.8, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.3, default_y=-380.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=361.69):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=222.99):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=197.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=275.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=250.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=258.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=208.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=319.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=204.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=254.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=481.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=234.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=251.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(130.52)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=152.33):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=213.95):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=130.5):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=87.47, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='30', width=217.46):
            with Note(default_x=15.8, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.97, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=85.95, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=112.93, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=156.1, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=183.08, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='31', width=146.86):
            with Note(default_x=15.8, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=48.16, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Note(default_x=80.53, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.52, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja!')
            with Note(default_x=112.89, default_y=-494.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='32', width=153.24):
            with Note(default_x=16.16, default_y=-494.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=54.38, default_y=-484.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.05, default_y=-489.25):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.71, default_y=-494.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=118.68, default_y=-489.25):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.64)
            with Note(default_x=102.94, default_y=-287.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=146.75, default_y=-292.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
                    Extend()
            with Note(default_x=163.93, default_y=-297.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.88, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=221.66, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='34', width=227.52):
            with Note(default_x=24.3, default_y=-287.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=69.1, default_y=-277.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=113.91, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=169.91, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='35', width=190.55):
            with Note(default_x=27.83, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.05, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=108.13, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=156.17, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='36', width=215.8):
            with Note(default_x=24.3, default_y=-267.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=83.47, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=122.25, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=181.42, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='37', width=223.48):
            with Note(default_x=28.19, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.41, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=84.75, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
            with Note(default_x=113.74, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.12, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=189.1, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='38', width=222.63):
            with Note(default_x=15.8, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=60.3, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=88.12, default_y=-302.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=115.94, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.44, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=188.26, default_y=-282.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.4)
            with Note(default_x=98.78, default_y=-274.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=150.0, default_y=-274.8):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.54, default_y=-41.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=245.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=174.59):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='1', width=157.65):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=174.19):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=189.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=247.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=167.15):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=228.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.14)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Note(default_x=184.36, default_y=-492.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='8', width=234.94):
            with Note(default_x=15.8, default_y=-512.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=63.48, default_y=-512.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=93.28, default_y=-512.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=123.09, default_y=-527.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=170.77, default_y=-527.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=200.57, default_y=-527.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='9', width=268.15):
            with Note(default_x=15.8, default_y=-512.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.3, default_y=-512.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=361.69):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=222.99):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=197.86):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=275.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=250.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=258.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=208.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=319.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=204.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=254.45):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=481.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=234.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=251.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(135.31)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=152.33):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=213.95):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=130.5):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=87.47, default_y=-634.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
        with Measure(number='30', width=217.46):
            with Note(default_x=15.8, default_y=-634.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=58.97, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=85.95, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=112.93, default_y=-634.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=156.1, default_y=-669.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=183.08, default_y=-669.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='31', width=146.86):
            with Note(default_x=15.8, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=48.16, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Note(default_x=80.53, default_y=-669.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.52, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja!')
            with Note(default_x=112.89, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
        with Measure(number='32', width=153.24):
            with Note(default_x=15.8, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=85.71, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=118.68, default_y=-654.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.02)
            with Note(default_x=102.94, default_y=-416.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=146.75, default_y=-421.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
                    Extend()
            with Note(default_x=163.93, default_y=-426.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.88, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=221.66, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='34', width=227.52):
            with Note(default_x=24.3, default_y=-416.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=69.1, default_y=-406.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=113.91, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=169.91, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='35', width=190.55):
            with Note(default_x=27.83, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.77, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=108.13, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=156.17, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
        with Measure(number='36', width=215.8):
            with Note(default_x=24.3, default_y=-396.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=83.47, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer,')
            with Note(default_x=122.25, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('theu')
            with Note(default_x=181.42, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('rer')
        with Measure(number='37', width=223.48):
            with Note(default_x=28.19, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.41, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fürst!')
            with Note(default_x=84.75, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er')
            with Note(default_x=113.74, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.12, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=189.1, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='38', width=222.63):
            with Note(default_x=15.8, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=60.3, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=88.12, default_y=-431.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=115.94, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=160.44, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-46.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,')
            with Note(default_x=188.26, default_y=-411.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.04)
            with Note(default_x=98.78, default_y=-366.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
            with Note(default_x=150.0, default_y=-366.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.54, default_y=-44.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('be!')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='40', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=249.46):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=245.81):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='43', width=174.59):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='0', implicit='yes', width=156.42):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(143.59)
                with StaffLayout(number=2):
                    StaffDistance(65.38)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=124.88, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.88, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=124.88, default_y=-298.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=124.88, default_y=-263.97):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='1', width=157.65):
            with Note(default_x=16.16, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=16.16, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=56.0, default_y=-163.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.0, default_y=-153.59):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=71.67, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=71.67, default_y=-158.59):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=87.33, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=87.33, default_y=-163.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=121.69, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=121.69, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-298.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-263.97):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=87.33, default_y=-298.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=87.33, default_y=-263.97):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=121.69, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=174.19):
            with Note(default_x=12.0, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=103.31, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.31, default_y=-163.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=137.95, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.95, default_y=-158.59):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=103.31, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.95, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=189.82):
            with Note(default_x=13.18, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.18, default_y=-158.59):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=114.04, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.04, default_y=-163.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=151.13, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=151.13, default_y=-163.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.18, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=114.04, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=151.13, default_y=-228.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=247.37):
            with Note(default_x=24.3, default_y=-183.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=24.3, default_y=-158.59):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=79.67, default_y=-178.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=79.67, default_y=-158.59):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=135.03, default_y=-178.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.03, default_y=-153.59):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=190.4, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=190.4, default_y=-143.59):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=24.3, default_y=-248.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=79.67, default_y=-248.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=135.03, default_y=-243.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=190.4, default_y=-243.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='5', width=167.15):
            with Note(default_x=12.0, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-143.59):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=54.65, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.65, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=97.31, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=97.31, default_y=-143.59):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=54.65, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=97.31, default_y=-278.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=97.31, default_y=-243.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=228.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.51, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.18, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.18, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=66.67, default_y=-173.59):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=66.67, default_y=-148.59):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.27, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=120.17, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=120.17, default_y=-143.59):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=173.67, default_y=-168.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=173.67, default_y=-143.59):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.18, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.18, default_y=-243.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.67, default_y=-263.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=66.67, default_y=-243.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=120.17, default_y=-278.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.17, default_y=-243.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=173.67, default_y=-278.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=173.67, default_y=-243.97):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='7', width=233.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.21)
                with StaffLayout(number=2):
                    StaffDistance(66.4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.51, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=98.78, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=98.78, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=141.75, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.75, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=184.36, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=184.36, default_y=-637.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=184.36, default_y=-627.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.78, default_y=-748.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=98.78, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=141.75, default_y=-748.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=141.75, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=184.36, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=184.36, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=234.94):
            with Note(default_x=15.8, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=63.48, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.48, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.28, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=93.28, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=123.09, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=123.09, default_y=-627.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=170.77, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.77, default_y=-627.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=200.57, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=200.57, default_y=-627.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-748.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-713.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=63.48, default_y=-783.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=63.48, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=93.28, default_y=-783.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=93.28, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=123.09, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.09, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.77, default_y=-798.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.77, default_y=-763.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=200.57, default_y=-798.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=200.57, default_y=-763.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=268.15):
            with Note(default_x=15.8, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.3, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.3, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=100.81, default_y=-627.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.47, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.79, default_y=-647.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.11, default_y=-642.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.43, default_y=-637.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.75, default_y=-632.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.07, default_y=-627.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.39, default_y=-622.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-783.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.3, default_y=-783.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.3, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=100.81, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.81, default_y=-753.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.81, default_y=-743.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=185.43, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=185.43, default_y=-753.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=185.43, default_y=-743.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=224.07, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=224.07, default_y=-753.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=224.07, default_y=-743.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=361.69):
            with Note(default_x=12.0, default_y=-632.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.67, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.97, default_y=-647.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.27, default_y=-642.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.58, default_y=-637.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.88, default_y=-632.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.19, default_y=-627.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.49, default_y=-622.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=187.79, default_y=-627.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.1, default_y=-652.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.4, default_y=-647.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.7, default_y=-642.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.01, default_y=-637.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.31, default_y=-632.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.62, default_y=-627.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.92, default_y=-622.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-738.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=102.58, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=102.58, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=102.58, default_y=-738.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=145.19, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=145.19, default_y=-748.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=145.19, default_y=-738.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=187.79, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.79, default_y=-753.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.79, default_y=-743.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=273.01, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=273.01, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=315.62, default_y=-763.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=315.62, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=222.99):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-78.99)
                Staff(1)
            with Note(default_x=12.0, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.33, default_y=-657.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.33, default_y=-632.5):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=91.69, default_y=-662.5):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=111.01, default_y=-652.5):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.73, default_y=-632.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=182.5, default_y=-637.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.22, default_y=-642.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-748.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-728.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=62.33, default_y=-758.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=62.33, default_y=-723.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=122.73, default_y=-743.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=122.73, default_y=-733.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=122.73, default_y=-723.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='12', width=338.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(150.32)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.9, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.02, default_y=-175.32):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=157.15, default_y=-165.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=186.27, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.4, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=244.52, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=273.65, default_y=-195.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.77, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=128.02, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=128.02, default_y=-245.32):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=128.02, default_y=-235.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=157.15, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.15, default_y=-245.32):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=157.15, default_y=-235.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=186.27, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=186.27, default_y=-245.32):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=186.27, default_y=-235.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=215.4, default_y=-250.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=215.4, default_y=-240.32):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=273.65, default_y=-285.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=273.65, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=197.86):
            with Note(default_x=12.0, default_y=-190.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.01, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.03, default_y=-190.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.04, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=104.05, default_y=-200.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=104.05, default_y=-190.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=127.07, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.08, default_y=-200.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.08, default_y=-190.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.09, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-280.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.03, default_y=-280.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.03, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=104.05, default_y=-290.32):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=104.05, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=150.08, default_y=-290.32):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=150.08, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=275.61):
            with Note(default_x=12.0, default_y=-195.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=44.13, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.25, default_y=-195.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.38, default_y=-160.32):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.51, default_y=-165.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.63, default_y=-150.32):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.76, default_y=-155.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=236.88, default_y=-165.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-290.32):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-265.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=108.38, default_y=-250.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=108.38, default_y=-240.32):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=140.51, default_y=-255.32):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.51, default_y=-245.32):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=172.63, default_y=-230.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.76, default_y=-255.32):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.76, default_y=-245.32):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=236.88, default_y=-230.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=250.81):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=16.16, default_y=-165.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.07, default_y=-160.32):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=69.98, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=96.89, default_y=-165.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.76, default_y=-160.32):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.56, default_y=-155.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=168.47, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.38, default_y=-155.32):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.29, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-310.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(1, type='start')
            with Note(default_x=15.8, default_y=-300.32):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
            with Note(default_x=69.62, default_y=-290.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(1, type='stop')
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=141.56, default_y=-260.32):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=195.38, default_y=-260.32):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=258.45):
            with Note(default_x=16.16, default_y=-150.32):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.86, default_y=-160.32):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.57, default_y=-170.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.27, default_y=-185.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=134.97, default_y=-200.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=134.97, default_y=-190.32):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=134.97, default_y=-175.32):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=224.08, default_y=-195.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=224.08, default_y=-170.32):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-250.32):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-240.32):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=134.97, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=224.08, default_y=-265.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=334.26):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(151.9)
                with StaffLayout(number=2):
                    StaffDistance(77.02)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.33, default_y=-161.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.52, default_y=-146.9):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=186.71, default_y=-151.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.9, default_y=-151.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=245.09, default_y=-156.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.28, default_y=-166.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=303.47, default_y=-161.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=128.33, default_y=-263.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.52, default_y=-248.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.71, default_y=-253.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.9, default_y=-253.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=245.09, default_y=-258.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.28, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=303.47, default_y=-263.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.78, default_y=-278.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=215.54, default_y=-278.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=208.8):
            with Note(default_x=12.0, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-166.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.7, default_y=-196.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.7, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.57, default_y=-196.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=88.57, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=112.42, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=112.42, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=174.42, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=174.42, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-263.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.85, default_y=-298.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.7, default_y=-263.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.57, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=112.42, default_y=-273.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=174.42, default_y=-273.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=319.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=26.37, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=26.37, default_y=-166.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=122.09, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=122.09, default_y=-166.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=158.9, default_y=-186.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.9, default_y=-166.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.04, default_y=-176.9):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=198.9, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=198.9, default_y=-161.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=240.98, default_y=-181.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.98, default_y=-171.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=240.98, default_y=-156.9):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=280.98, default_y=-186.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=280.98, default_y=-166.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=280.98, default_y=-151.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=26.37, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=122.09, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=158.9, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=198.9, default_y=-278.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.98, default_y=-273.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.98, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='20', width=204.45):
            with Note(default_x=15.5, default_y=-156.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.34, default_y=-161.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=109.18, default_y=-156.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.5, default_y=-181.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.92, default_y=-171.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.34, default_y=-186.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.76, default_y=-171.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.18, default_y=-171.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.6, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.02, default_y=-171.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.44, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.5, default_y=-263.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=85.76, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=108.82, default_y=-273.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=254.45):
            with Note(default_x=12.0, default_y=-176.9):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.11, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.21, default_y=-181.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.32, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.43, default_y=-186.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=162.53, default_y=-206.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=192.64, default_y=-191.9):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.75, default_y=-206.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-268.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.21, default_y=-283.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=132.43, default_y=-288.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=192.64, default_y=-283.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=353.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(151.92)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-191.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.04, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=159.3, default_y=-196.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.56, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=231.11, default_y=-196.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.11, default_y=-176.92):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=261.38, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.64, default_y=-191.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.64, default_y=-181.92):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=321.9, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.78, default_y=-286.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=189.56, default_y=-261.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.11, default_y=-266.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=291.64, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=481.58):
            with Note(default_x=30.5, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=30.5, default_y=-191.92):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=30.5, default_y=-181.92):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=238.16, default_y=-206.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=238.16, default_y=-196.92):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=238.16, default_y=-186.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.51, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=370.21, default_y=-181.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=370.21, default_y=-171.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=370.21, default_y=-156.92):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=30.5, default_y=-286.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=238.16, default_y=-286.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=370.21, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='24', width=234.87):
            with Note(default_x=12.0, default_y=-181.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-171.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-156.92):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=125.99, default_y=-181.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=125.99, default_y=-171.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=179.63, default_y=-176.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=179.63, default_y=-166.92):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=125.99, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=179.63, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='25', width=251.16):
            with Note(default_x=13.18, default_y=-176.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.18, default_y=-166.92):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=136.02, default_y=-181.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=136.02, default_y=-171.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=192.79, default_y=-181.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.79, default_y=-171.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.18, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=136.02, default_y=-271.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=192.79, default_y=-236.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='26', width=307.03):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.58)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.78, default_y=-806.13):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=150.44, default_y=-826.13):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=150.44, default_y=-806.13):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=202.11, default_y=-826.13):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.11, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=253.77, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=253.77, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.78, default_y=-896.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=150.44, default_y=-896.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=202.11, default_y=-891.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=253.77, default_y=-891.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='27', width=152.33):
            with Note(default_x=12.0, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.54, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=50.54, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=89.07, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=89.07, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=12.0, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=50.54, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=89.07, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.07, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='28', width=213.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.51, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.18, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.18, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.67, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=61.67, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=112.33, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.33, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=160.82, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=160.82, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.18, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.18, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=61.67, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=61.67, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=112.33, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=112.33, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=160.82, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=160.82, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='29', width=130.5):
            with Note(default_x=13.18, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.18, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.51, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=50.51, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=87.47, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=87.47, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=87.47, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.18, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.18, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=50.51, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=50.51, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=87.47, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=87.47, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=217.46):
            with Note(default_x=15.8, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.97, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.97, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.95, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.95, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.93, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.93, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.93, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=156.1, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.1, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.1, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.08, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=183.08, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.08, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-876.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.97, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=58.97, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=85.95, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.95, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=112.93, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.93, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=156.1, default_y=-961.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=156.1, default_y=-926.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=183.08, default_y=-961.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=183.08, default_y=-926.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='31', width=146.86):
            with Note(default_x=15.8, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=48.16, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=48.16, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=80.53, default_y=-801.13):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=80.53, default_y=-791.13):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.89, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.89, default_y=-811.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.89, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=48.16, default_y=-911.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.16, default_y=-876.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.53, default_y=-926.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=4.42, relative_y=10.0)
            with Note(default_x=80.53, default_y=-891.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.89, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=112.89, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='32', width=153.24):
            with Note(default_x=16.16, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=16.16, default_y=-811.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=16.16, default_y=-796.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=54.38, default_y=-811.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=54.38, default_y=-801.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=70.05, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=70.05, default_y=-806.13):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=85.71, default_y=-821.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=85.71, default_y=-811.13):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.68, default_y=-816.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=118.68, default_y=-806.13):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=85.71, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.71, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=118.68, default_y=-946.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=118.68, default_y=-911.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='33', width=261.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(100.44)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=102.94, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=102.94, default_y=-572.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=146.75, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.75, default_y=-577.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=163.93, default_y=-592.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.93, default_y=-582.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=183.88, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.88, default_y=-577.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=221.66, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=221.66, default_y=-577.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=102.58, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=102.58, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=183.88, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=183.88, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=221.66, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=221.66, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='34', width=227.52):
            with Note(default_x=24.3, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=24.3, default_y=-572.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=69.1, default_y=-592.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=69.1, default_y=-572.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.91, default_y=-592.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.91, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.91, default_y=-597.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.91, default_y=-572.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.91, default_y=-592.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.91, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.91, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=197.91, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=24.3, default_y=-732.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=24.3, default_y=-697.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=69.1, default_y=-732.02):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=69.1, default_y=-697.02):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=113.91, default_y=-727.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=113.91, default_y=-692.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=169.91, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.91, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=190.55):
            with Note(default_x=28.19, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=28.19, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=68.74, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=68.74, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=108.13, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=108.13, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=156.17, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.17, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=27.83, default_y=-677.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=27.83, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=108.13, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=108.13, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=156.17, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=156.17, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=215.8):
            with Note(default_x=24.3, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=24.3, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=83.47, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=83.47, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=122.25, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=122.25, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=181.42, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=181.42, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=24.3, default_y=-677.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=24.3, default_y=-642.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=83.47, default_y=-677.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=122.25, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=122.25, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=181.42, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=223.48):
            with Note(default_x=28.19, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=28.19, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=84.75, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=84.75, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.74, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.74, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.74, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=160.12, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.12, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=160.12, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=189.1, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.1, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=189.1, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=28.19, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=28.19, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=84.75, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=84.75, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=113.74, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=160.12, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=189.1, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='38', width=222.63):
            with Note(default_x=15.8, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=60.3, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=60.3, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.12, default_y=-587.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=88.12, default_y=-562.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=115.94, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=115.94, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=115.94, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=160.44, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.44, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=160.44, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.26, default_y=-582.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=188.26, default_y=-567.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.26, default_y=-557.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-677.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-642.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.3, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=60.3, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=88.12, default_y=-712.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=88.12, default_y=-677.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=115.94, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=115.94, default_y=-657.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=160.44, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=188.26, default_y=-692.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='39', width=421.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.6)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-501.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=98.78, default_y=-476.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=150.0, default_y=-501.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.0, default_y=-476.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.26, default_y=-481.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.55, default_y=-476.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=233.83, default_y=-471.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.12, default_y=-466.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.4, default_y=-461.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.69, default_y=-466.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=326.97, default_y=-461.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=350.25, default_y=-456.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.54, default_y=-451.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=396.82, default_y=-446.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.78, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=98.78, default_y=-556.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.0, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.0, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=187.26, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=187.26, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=233.83, default_y=-606.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=233.83, default_y=-586.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=233.83, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=326.97, default_y=-606.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=326.97, default_y=-586.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=326.97, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=373.54, default_y=-606.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=373.54, default_y=-586.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=373.54, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=249.46):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-441.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=69.24, default_y=-446.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.5, default_y=-451.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.77, default_y=-456.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=161.85, default_y=-441.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='start')
            with Note(default_x=15.44, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
            with Note(default_x=68.88, default_y=-571.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='stop')
            with Note(default_x=161.85, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.85, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.8, default_y=-566.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.75, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.75, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=224.69, default_y=-566.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=249.46):
            with Note(default_x=15.8, default_y=-441.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=69.24, default_y=-446.44):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.5, default_y=-451.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.77, default_y=-456.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=161.85, default_y=-441.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='start')
            with Note(default_x=15.44, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
            with Note(default_x=68.88, default_y=-571.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='stop')
            with Note(default_x=161.85, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.85, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.8, default_y=-566.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.75, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.75, default_y=-576.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=224.69, default_y=-566.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=245.81):
            with Note(default_x=15.8, default_y=-456.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=81.22, default_y=-461.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.85, default_y=-466.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.49, default_y=-456.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=185.91, default_y=-461.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=205.38, default_y=-466.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.04, default_y=-471.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(48.0)
            with Note(default_x=15.44, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='start')
            with Note(default_x=15.44, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
            with Note(default_x=52.51, default_y=-571.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='stop')
            with Note(default_x=120.13, default_y=-606.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='start')
            with Note(default_x=120.13, default_y=-586.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
            with Note(default_x=157.2, default_y=-571.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        Tremolo(2, type='stop')
        with Measure(number='43', width=174.59):
            with Note(default_x=12.0, default_y=-476.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.93, default_y=-466.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.93, default_y=-456.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.93, default_y=-441.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.93, default_y=-431.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.86, default_y=-476.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.86, default_y=-466.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.86, default_y=-456.44):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.86, default_y=-441.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(36.0)
            with Note(default_x=12.0, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-581.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=62.93, default_y=-591.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=62.93, default_y=-556.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=113.86, default_y=-626.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=113.86, default_y=-591.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=9.0, relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')