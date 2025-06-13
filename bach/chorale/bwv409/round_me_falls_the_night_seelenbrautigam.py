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
            Millimeters(5.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2120.9)
            PageWidth(1500.41)
            with PageMargins(type='even'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
            with PageMargins(type='odd'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Midi_74', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Midi_74', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Midi_74', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Midi_74', print_object='no')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=514.17):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.04)
                        RightMargin(-0.0)
                    TopSystemDistance(378.5)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=139.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Sound(tempo=90.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Round me falls the night', default_y=1.72, relative_y=20.0, font_family='Times New Roman', font_size='19')
            with Direction(placement='above'):
                with DirectionType():
                    Words('William Romanis\n', default_y=64.17, relative_y=20.0, font_family='Times New Roman', font_size='11')
                    Words('(1824-99)')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adam Drese (1620-1701)\n', default_y=115.53, relative_y=20.0, font_family='Times New Roman', font_size='11')
                    Words('harmonised by J. S. Bach (1685-1750)')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=171.4, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Sound(tempo=90.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=203.11, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Sound(tempo=90.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=234.82, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Sound(tempo=90.0)
            with Note(default_x=123.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-9.74, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('      Round')
                with Lyric(number='2', default_x=-4.59, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('    Earth')
                with Lyric(number='3', default_x=-4.7, default_y=-94.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('    Bless')
            with Note(default_x=225.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
            with Note(default_x=328.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('falls')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('work')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('heaven')
            with Note(default_x=410.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
        with Measure(number='2', width=379.86):
            with Note(default_x=26.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('night;')
                with Lyric(number='2', default_x=9.1, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('done,')
                with Lyric(number='3', default_x=6.22, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('Light')
            with Note(default_x=151.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Earth')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Shin')
            with Note(default_x=265.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('viour')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing')
        with Measure(number='3', width=457.49):
            with Note(default_x=33.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('sounds')
                with Lyric(number='3', default_x=8.32, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("thro'")
            with Note(default_x=160.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('are')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("earth's")
            with Note(default_x=224.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=287.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('light')
                with Lyric(number='2', default_x=9.21, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('none;')
                with Lyric(number='3', default_x=8.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('night:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='4', width=440.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.04)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=153.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.52, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text("Thro'")
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rest')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Voice')
            with Note(default_x=233.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
            with Note(default_x=296.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('hours')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=359.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
        with Measure(number='5', width=305.3):
            with Note(default_x=23.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dark')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('si')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('love')
            with Note(default_x=96.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('ness')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('lence')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('has')
            with Note(default_x=169.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('shroud')
                with Lyric(number='2', default_x=6.94, default_y=-67.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('seek')
                with Lyric(number='3', default_x=6.94, default_y=-90.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('told')
        with Measure(number='6', width=249.25):
            with Note(default_x=16.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
                with Lyric(number='2', default_x=8.67, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing,')
                with Lyric(number='3', default_x=8.79, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Note(default_x=132.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Arms')
            with Note(default_x=190.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
        with Measure(number='7', width=356.08):
            with Note(default_x=30.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hear')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('strong')
            with Note(default_x=97.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('thy')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=186.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('face')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('soft')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('clasp')
            with Note(default_x=270.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-67.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-90.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
        with Measure(number='8', width=390.6):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.04)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=101.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cloud')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('speak')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('end')
                    Text('hold')
            with Note(default_x=219.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.48, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed;')
                with Lyric(number='2', default_x=9.28, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing;')
                with Lyric(number='3', default_x=9.15, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Note(default_x=257.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=349.97):
            with Note(default_x=26.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thou')
            with Note(default_x=98.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
            with Note(default_x=187.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('spi')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('end')
                    Text('watch')
            with Note(default_x=259.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('ry')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text("rit's")
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('wilt')
        with Measure(number='10', width=303.52):
            with Note(default_x=25.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('shine')
                with Lyric(number='2', default_x=6.22, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('ear')
                with Lyric(number='3', default_x=8.84, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('keep,')
            with Note(default_x=148.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Whi')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Sa')
            with Note(default_x=225.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('end')
                    Text('this')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('sper')
                with Lyric(number='3', default_x=9.08, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('viour,')
        with Measure(number='11', width=307.43):
            with Note(default_x=25.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('heart')
                with Lyric(number='2', default_x=4.83, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text("'I")
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'er")
            with Note(default_x=116.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='3', default_x=6.58, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=161.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-43.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='2', default_x=10.92, default_y=-66.85, relative_y=-30.0):
                    Syllabic('single')
                    Text("near.'")
                with Lyric(number='3', default_x=8.61, default_y=-90.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=514.17):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(118.11)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=123.52, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-9.74, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('      Round')
                with Lyric(number='2', default_x=-4.59, default_y=-75.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('    Earth')
                with Lyric(number='3', default_x=-4.7, default_y=-98.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('    Bless')
            with Note(default_x=225.9, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
            with Note(default_x=328.28, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('falls')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('work')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('heaven')
            with Note(default_x=410.19, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
            with Note(default_x=461.38, default_y=-193.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=379.86):
            with Note(default_x=26.99, default_y=-188.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('night;')
                with Lyric(number='2', default_x=9.1, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('done,')
                with Lyric(number='3', default_x=6.22, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Light')
            with Note(default_x=151.87, default_y=-193.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Earth')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Shin')
            with Note(default_x=265.06, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('viour')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing')
        with Measure(number='3', width=457.49):
            with Note(default_x=33.15, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('sounds')
                with Lyric(number='3', default_x=8.32, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("thro'")
            with Note(default_x=160.52, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='2', default_x=6.58, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('are')
                with Lyric(number='3', default_x=6.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("earth's")
            with Note(default_x=287.52, default_y=-198.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('light')
                with Lyric(number='2', default_x=9.21, default_y=-75.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('none;')
                with Lyric(number='3', default_x=8.58, default_y=-98.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('night:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='4', width=440.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(119.03)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=153.68, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.52, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text("Thro'")
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rest')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('Voice')
            with Note(default_x=233.01, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
            with Note(default_x=296.48, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('hours')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=399.62, default_y=-179.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
        with Measure(number='5', width=305.3):
            with Note(default_x=23.07, default_y=-179.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.16, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dark-')
                with Lyric(number='2', default_x=10.02, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('si-')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('love')
            with Note(default_x=59.88, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=96.68, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ness')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('lence')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('has')
            with Note(default_x=133.48, default_y=-179.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=170.29, default_y=-179.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.28, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('shroud-')
                with Lyric(number='2', default_x=10.42, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('seek-')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('told')
            with Note(default_x=207.09, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=230.09, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.1, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=249.25):
            with Note(default_x=17.1, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=74.73, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
                with Lyric(number='2', default_x=9.03, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing,')
                with Lyric(number='3', default_x=9.15, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Note(default_x=132.37, default_y=-194.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('Arms')
            with Note(default_x=190.01, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
        with Measure(number='7', width=356.08):
            with Note(default_x=30.38, default_y=-184.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('hear')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('strong')
            with Note(default_x=97.71, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('thy')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=186.14, default_y=-189.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.23, default_y=-194.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('face')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('soft')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('end')
                    Text('clasp')
            with Note(default_x=312.4, default_y=-199.03):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-68.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-92.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
        with Measure(number='8', width=390.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.36)
            with Note(default_x=101.57, default_y=-189.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.37, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('cloud-')
                with Lyric(number='2', default_x=10.28, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('speak-')
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('hold')
            with Note(default_x=140.72, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=179.86, default_y=-189.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.14, default_y=-189.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=320.77, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.48, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed;')
                with Lyric(number='2', default_x=9.28, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing;')
                with Lyric(number='3', default_x=8.9, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('me:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=349.97):
            with Note(default_x=26.85, default_y=-189.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thou')
            with Note(default_x=98.3, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
            with Note(default_x=187.61, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('spi')
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('end')
                    Text('watch')
            with Note(default_x=259.06, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('ry')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text("rit's")
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('wilt')
        with Measure(number='10', width=303.52):
            with Note(default_x=25.73, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('shine')
                with Lyric(number='2', default_x=6.22, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('ear')
                with Lyric(number='3', default_x=8.84, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('keep,')
            with Note(default_x=148.68, default_y=-204.36):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='2', default_x=9.91, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Whi-')
                with Lyric(number='3', default_x=10.01, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sa-')
            with Note(default_x=186.99, default_y=-189.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.3, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('this')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('sper')
                with Lyric(number='3', default_x=9.08, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('viour,')
        with Measure(number='11', width=307.43):
            with Note(default_x=25.84, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('heart')
                with Lyric(number='2', default_x=4.83, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text("'I")
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'er")
            with Note(default_x=71.01, default_y=-179.36):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.17, default_y=-184.36):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='3', default_x=6.58, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=217.43, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-60.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='2', default_x=10.92, default_y=-84.35, relative_y=-30.0):
                    Syllabic('single')
                    Text("near.'")
                with Lyric(number='3', default_x=8.61, default_y=-107.92, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=514.17):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(121.53)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=123.52, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=-9.74, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('      Round')
                with Lyric(number='2', default_x=-4.59, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('    Earth')
                with Lyric(number='3', default_x=-4.7, default_y=-94.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('    Bless')
            with Note(default_x=225.9, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
            with Note(default_x=328.28, default_y=-339.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('falls')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('work')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('heaven')
            with Note(default_x=410.19, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
        with Measure(number='2', width=379.86):
            with Note(default_x=26.99, default_y=-324.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.56, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('night;')
                with Lyric(number='2', default_x=9.82, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('done,')
                with Lyric(number='3', default_x=6.94, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('Light')
            with Note(default_x=151.87, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.01, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sa-')
                with Lyric(number='2', default_x=9.74, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Earth-')
                with Lyric(number='3', default_x=10.13, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('Shin-')
            with Note(default_x=208.47, default_y=-329.64):
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
            with Note(default_x=265.06, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('viour')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing')
            with Note(default_x=321.66, default_y=-339.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=457.49):
            with Note(default_x=33.15, default_y=-339.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=96.83, default_y=-344.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('sounds')
                with Lyric(number='3', default_x=8.32, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("thro'")
            with Note(default_x=224.2, default_y=-349.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('are')
                with Lyric(number='3', default_x=6.58, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("earth's")
            with Note(default_x=287.52, default_y=-334.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('light')
                with Lyric(number='2', default_x=9.93, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('none;')
                with Lyric(number='3', default_x=9.31, default_y=-94.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('night:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='4', width=440.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(120.85)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef(after_barline='yes'):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=153.68, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.52, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text("Thro'")
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rest')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Voice')
            with Note(default_x=233.01, default_y=-319.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
            with Note(default_x=296.48, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('hours')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=359.95, default_y=-319.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
            with Note(default_x=399.62, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=305.3):
            with Note(default_x=23.07, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dark')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('si')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('end')
                    Text('love')
            with Note(default_x=96.68, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ness')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('lence')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('has')
            with Note(default_x=169.93, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-54.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('shroud')
                with Lyric(number='2', default_x=6.94, default_y=-77.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('seek')
                with Lyric(number='3', default_x=6.94, default_y=-101.27, relative_y=-30.0):
                    Syllabic('end')
                    Text('told')
        with Measure(number='6', width=249.25):
            with Note(default_x=16.73, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
                with Lyric(number='2', default_x=9.39, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing,')
                with Lyric(number='3', default_x=9.51, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Note(default_x=132.37, default_y=-334.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Arms')
            with Note(default_x=190.01, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
        with Measure(number='7', width=356.08):
            with Note(default_x=30.38, default_y=-324.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hear')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('strong')
            with Note(default_x=139.8, default_y=-329.87):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('thy')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=186.14, default_y=-334.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('face')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('soft')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('end')
                    Text('clasp')
            with Note(default_x=270.31, default_y=-334.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-77.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-101.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
        with Measure(number='8', width=390.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(139.65)
            with Note(default_x=101.21, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cloud')
                with Lyric(number='2', default_x=6.94, default_y=-73.76, relative_y=-30.0):
                    Syllabic('middle')
                    Text('speak')
                with Lyric(number='3', default_x=6.94, default_y=-97.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('hold')
            with Note(default_x=257.78, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.85, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed;')
                with Lyric(number='2', default_x=9.64, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing;')
                with Lyric(number='3', default_x=9.51, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=349.97):
            with Note(default_x=26.85, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thou')
            with Note(default_x=98.3, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
            with Note(default_x=187.61, default_y=-354.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('middle')
                    Text('spi')
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('end')
                    Text('watch')
            with Note(default_x=259.06, default_y=-359.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('ry')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("rit's")
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('wilt')
        with Measure(number='10', width=303.52):
            with Note(default_x=26.1, default_y=-359.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('shine')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('ear')
                with Lyric(number='3', default_x=9.2, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('keep,')
            with Note(default_x=87.39, default_y=-364.01):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.68, default_y=-359.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='2', default_x=9.91, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Whi-')
                with Lyric(number='3', default_x=10.01, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sa-')
            with Note(default_x=186.99, default_y=-344.01):
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
            with Note(default_x=225.3, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('this')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('sper')
                with Lyric(number='3', default_x=9.08, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('viour,')
            with Note(default_x=263.61, default_y=-354.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=307.43):
            with Note(default_x=25.84, default_y=-359.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('heart')
                with Lyric(number='2', default_x=4.83, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("'I")
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'er")
            with Note(default_x=71.01, default_y=-339.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.17, default_y=-339.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='3', default_x=6.58, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=189.57, default_y=-344.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.43, default_y=-349.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.08, default_y=-50.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='2', default_x=11.64, default_y=-73.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("near.'")
                with Lyric(number='3', default_x=9.33, default_y=-97.33, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=514.17):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(119.54)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=123.52, default_y=-514.18):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=-9.74, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('      Round')
                with Lyric(number='2', default_x=-1.32, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('    Earth-')
                with Lyric(number='3', default_x=-1.17, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('    Bless-')
            with Note(default_x=174.71, default_y=-509.18):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.9, default_y=-504.18):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
            with Note(default_x=277.09, default_y=-499.18):
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
            with Note(default_x=328.28, default_y=-494.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('falls')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('work')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('heaven')
            with Note(default_x=410.19, default_y=-514.18):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
        with Measure(number='2', width=379.86):
            with Note(default_x=26.99, default_y=-494.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.56, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('night;')
                with Lyric(number='2', default_x=9.82, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('done,')
                with Lyric(number='3', default_x=6.94, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('Light')
            with Note(default_x=151.87, default_y=-489.18):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Earth')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Shin')
            with Note(default_x=265.06, default_y=-484.18):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('viour')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing')
        with Measure(number='3', width=457.49):
            with Note(default_x=33.15, default_y=-479.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('sounds')
                with Lyric(number='3', default_x=8.32, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text("thro'")
            with Note(default_x=160.52, default_y=-494.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='2', default_x=6.58, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('are')
                with Lyric(number='3', default_x=6.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text("earth's")
            with Note(default_x=287.52, default_y=-514.18):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('light')
                with Lyric(number='2', default_x=9.21, default_y=-71.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('none;')
                with Lyric(number='3', default_x=8.58, default_y=-95.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('night:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='4', width=440.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(132.4)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=153.68, default_y=-492.27):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.52, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text("Thro'")
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rest')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Voice')
            with Note(default_x=193.35, default_y=-497.27):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=233.01, default_y=-502.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
            with Note(default_x=296.48, default_y=-517.27):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('hours')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('oft')
            with Note(default_x=359.95, default_y=-502.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
            with Note(default_x=399.62, default_y=-497.27):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=305.3):
            with Note(default_x=23.07, default_y=-492.27):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dark')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('si')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('love')
            with Note(default_x=96.68, default_y=-507.27):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ness')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('lence')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('has')
            with Note(default_x=133.48, default_y=-497.27):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=170.29, default_y=-492.27):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.28, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('shroud-')
                with Lyric(number='2', default_x=10.42, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('seek-')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('told')
            with Note(default_x=253.1, default_y=-527.27):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=249.25):
            with Note(default_x=16.73, default_y=-507.27):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed')
                with Lyric(number='2', default_x=9.39, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing,')
                with Lyric(number='3', default_x=9.51, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Note(default_x=132.37, default_y=-502.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Arms')
            with Note(default_x=190.01, default_y=-507.27):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
        with Measure(number='7', width=356.08):
            with Note(default_x=30.38, default_y=-492.27):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('hear')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('strong')
            with Note(default_x=97.71, default_y=-507.27):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('thy')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=186.14, default_y=-502.27):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('face')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('soft')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('clasp')
            with Note(default_x=270.31, default_y=-517.27):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='2', default_x=6.58, default_y=-68.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-91.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
        with Measure(number='8', width=390.6):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(127.83)
            with Note(default_x=101.57, default_y=-546.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.37, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('cloud-')
                with Lyric(number='2', default_x=10.28, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('speak-')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('hold')
            with Note(default_x=140.72, default_y=-541.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.86, default_y=-536.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=219.0, default_y=-531.84):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=257.78, default_y=-526.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.12, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ed;')
                with Lyric(number='2', default_x=8.92, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('ing;')
                with Lyric(number='3', default_x=8.79, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=349.97):
            with Note(default_x=26.85, default_y=-511.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thou')
            with Note(default_x=98.3, default_y=-526.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy')
            with Note(default_x=142.96, default_y=-521.84):
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
            with Note(default_x=187.61, default_y=-516.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('glo')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('middle')
                    Text('spi')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('watch')
            with Note(default_x=259.06, default_y=-526.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ry')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text("rit's")
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('wilt')
            with Note(default_x=303.72, default_y=-536.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=303.52):
            with Note(default_x=25.73, default_y=-516.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('shine')
                with Lyric(number='2', default_x=6.94, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('ear')
                with Lyric(number='3', default_x=9.56, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('keep,')
            with Note(default_x=148.68, default_y=-511.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('In')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Whi')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Sa')
            with Note(default_x=225.3, default_y=-506.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('this')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sper')
                with Lyric(number='3', default_x=9.08, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('viour,')
        with Measure(number='11', width=307.43):
            with Note(default_x=25.84, default_y=-501.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('heart')
                with Lyric(number='2', default_x=4.83, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text("'I")
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'er")
            with Note(default_x=116.17, default_y=-516.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='3', default_x=6.58, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=217.43, default_y=-536.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.36, default_y=-59.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='2', default_x=10.92, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text("near.'")
                with Lyric(number='3', default_x=8.61, default_y=-106.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep.')
            with Barline(location='right'):
                BarStyle('light-heavy')