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
            Millimeters(7.52)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1579.39)
            PageWidth(1117.33)
            with PageMargins(type='even'):
                LeftMargin(53.1915)
                RightMargin(53.1915)
                TopMargin(53.1915)
                BottomMargin(106.383)
            with PageMargins(type='odd'):
                LeftMargin(53.1915)
                RightMargin(53.1915)
                TopMargin(53.1915)
                BottomMargin(106.383)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Midi_74', print_object='no')
            PartAbbreviation(' ')
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
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=160.07):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.25)
                        RightMargin(-0.0)
                    TopSystemDistance(174.16)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
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
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, default_y=30.9, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Note(default_x=111.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Backup():
                Duration(2.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
            with Backup():
                Duration(2.0)
            with Note(default_x=111.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=206.57):
            with Note(default_x=12.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
            with Note(default_x=110.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=142.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=142.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=152.13):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.32, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
                with Lyric(number='2', default_x=9.32, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
                with Lyric(number='3', default_x=9.32, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
            with Direction(placement='above'):
                with DirectionType():
                    Words('O Jesulein süß', relative_y=20.0, font_family='Times New Roman', font_size='20')
            with Note(default_x=114.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=50.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=160.53):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
            with Note(default_x=55.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=107.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=80.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
            with Note(default_x=107.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='5', width=151.94):
            with Note(default_x=23.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
                with Lyric(number='2', default_x=8.66, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
                with Lyric(number='3', default_x=8.66, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
            with Note(default_x=101.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('Deins')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mit')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=101.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=173.45):
            with Direction(placement='above'):
                with DirectionType():
                    Words('arr. J.S. Bach', default_y=1.03, relative_y=20.0, font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    Words('(1685-1750)', default_y=24.41, relative_y=20.0, font_family='Times New Roman')
            with Note(default_x=23.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-82.11, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='2', default_x=6.22, default_y=-106.42, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Freu')
                with Lyric(number='3', default_x=6.22, default_y=-130.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('bist')
            with Note(default_x=123.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.11, relative_y=-30.0):
                    Syllabic('single')
                    Text('ters')
                with Lyric(number='2', default_x=6.58, default_y=-106.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='3', default_x=6.58, default_y=-130.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=98.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=123.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=147.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=277.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(16.25)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=90.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('Willn')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lieb')
            with Note(default_x=151.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=212.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=102.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=181.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=183.59):
            with Note(default_x=24.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('Welt')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('E')
            with Note(default_x=77.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ben')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=40.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=129.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=162.99):
            with Note(default_x=21.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-81.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('füllt;')
                with Lyric(number='2', default_x=8.47, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('füllt,')
                with Lyric(number='3', default_x=8.37, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('bild,')
            with Note(default_x=94.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('bist')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('zünd')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=94.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=206.61):
            with Note(default_x=38.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-81.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kom')
                with Lyric(number='2', default_x=6.22, default_y=-105.97, relative_y=-30.0):
                    Syllabic('end')
                    Text('kommst')
                with Lyric(number='3', default_x=6.22, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
            with Note(default_x=157.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('men')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('in')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=39.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=164.27):
            with Note(default_x=17.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
                with Lyric(number='2', default_x=6.22, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('ab')
                with Lyric(number='3', default_x=6.22, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=111.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
                with Lyric(number='2', default_x=6.58, default_y=-105.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('vom')
                with Lyric(number='3', default_x=6.58, default_y=-130.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=111.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=136.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=232.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(16.25)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=101.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-92.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.22, default_y=-116.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Him')
                with Lyric(number='3', default_x=6.22, default_y=-140.65, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Lie')
            with Note(default_x=184.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-92.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-116.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mels')
                with Lyric(number='3', default_x=6.58, default_y=-140.65, relative_y=-30.0):
                    Syllabic('end')
                    Text('be')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=101.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=138.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=207.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=174.58):
            with Note(default_x=34.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.2, default_y=-92.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich,')
                with Lyric(number='2', default_x=9.0, default_y=-116.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('saal,')
                with Lyric(number='3', default_x=8.46, default_y=-140.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('Flamm,')
            with Note(default_x=107.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-92.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='2', default_x=6.58, default_y=-116.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-140.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=34.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=107.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=164.66):
            with Note(default_x=25.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-92.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ar')
                with Lyric(number='2', default_x=6.22, default_y=-116.34, relative_y=-30.0):
                    Syllabic('end')
                    Text("tröst'st")
                with Lyric(number='3', default_x=6.22, default_y=-140.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('wir')
            with Note(default_x=120.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-92.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('men')
                with Lyric(number='2', default_x=6.58, default_y=-116.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='3', default_x=6.58, default_y=-140.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=25.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=67.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=218.02):
            with Note(default_x=23.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-92.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Men')
                with Lyric(number='2', default_x=6.22, default_y=-116.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('in')
                with Lyric(number='3', default_x=6.22, default_y=-140.65, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lie')
            with Note(default_x=145.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-92.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('schen')
                with Lyric(number='2', default_x=6.58, default_y=-116.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
                with Lyric(number='3', default_x=6.58, default_y=-140.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=35.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=205.2):
            with Note(default_x=20.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-92.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wor')
                with Lyric(number='2', default_x=6.22, default_y=-116.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Jam')
                with Lyric(number='3', default_x=6.22, default_y=-140.65, relative_y=-30.0):
                    Syllabic('middle')
                    Text('all')
            with Note(default_x=152.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-92.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                with Lyric(number='2', default_x=6.58, default_y=-116.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer')
                with Lyric(number='3', default_x=6.58, default_y=-140.65, relative_y=-30.0):
                    Syllabic('middle')
                    Text('zu')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=52.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=241.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(16.25)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=90.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.3, default_y=-89.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('gleich,')
                with Lyric(number='2', default_x=5.31, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('-tal,')
                with Lyric(number='3', default_x=7.63, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text("-samm',")
            with Note(default_x=190.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=102.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=140.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=229.99):
            with Note(default_x=12.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
            with Note(default_x=83.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=153.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=47.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.16, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=153.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=177.38):
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.32, default_y=-89.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
                with Lyric(number='2', default_x=9.32, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
                with Lyric(number='3', default_x=9.32, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('süß!')
            with Note(default_x=119.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Note(default_x=119.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=226.65):
            with Note(default_x=12.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('Je')
            with Note(default_x=118.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=154.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-89.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
                with Lyric(number='2', default_x=6.58, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
                with Lyric(number='3', default_x=6.58, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(6.0)
                Voice('2')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=189.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='21', width=118.89):
            with Note(default_x=23.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-89.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
                with Lyric(number='2', default_x=8.66, default_y=-113.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
                with Lyric(number='3', default_x=8.66, default_y=-137.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('mild!')
            with Backup():
                Duration(4.0)
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('2')
                Type('half')
            with Backup():
                Duration(4.0)
            with Note(default_x=23.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=160.07):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(194.5)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=111.43, default_y=-229.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(2.0)
            with Note(default_x=111.43, default_y=-229.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.95, default_y=-234.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=206.57):
            with Note(default_x=12.61, default_y=-229.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.77, default_y=-219.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.06, default_y=-219.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-239.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.77, default_y=-254.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.06, default_y=-239.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=173.51, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=152.13):
            with Note(default_x=14.0, default_y=-224.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=114.06, default_y=-224.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=14.36, default_y=-249.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=50.93, default_y=-254.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.6, default_y=-259.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.06, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=160.53):
            with Note(default_x=13.8, default_y=-219.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=80.76, default_y=-219.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=107.42, default_y=-239.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.17, default_y=-224.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-254.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.0, default_y=-264.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.42, default_y=-259.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=151.94):
            with Note(default_x=23.13, default_y=-234.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=101.55, default_y=-229.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.13, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=101.55, default_y=-264.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=173.45):
            with Note(default_x=23.68, default_y=-229.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.65, default_y=-234.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=123.25, default_y=-219.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.68, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=50.35, default_y=-249.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=74.65, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=123.25, default_y=-244.5):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='7', width=277.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(190.22)
            with Note(default_x=90.38, default_y=-215.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.37, default_y=-210.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=242.86, default_y=-210.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=90.38, default_y=-235.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=120.88, default_y=-240.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=151.37, default_y=-235.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=212.37, default_y=-230.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=183.59):
            with Note(default_x=24.45, default_y=-215.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.6, default_y=-220.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=24.81, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.2, default_y=-245.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.6, default_y=-240.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=162.99):
            with Note(default_x=21.45, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=94.92, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.45, default_y=-260.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=94.92, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=128.16, default_y=-230.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=206.61):
            with Note(default_x=39.07, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=127.96, default_y=-220.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.6, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=39.07, default_y=-235.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=98.33, default_y=-245.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.6, default_y=-255.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=164.27):
            with Note(default_x=18.05, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.37, default_y=-230.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=85.2, default_y=-225.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.02, default_y=-220.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.69, default_y=-240.22):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=111.02, default_y=-230.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=136.84, default_y=-235.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=232.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(194.18)
            with Note(default_x=101.58, default_y=-229.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=184.53, default_y=-234.18):
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
                Duration(6.0)
            with Note(default_x=101.95, default_y=-244.18):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=138.65, default_y=-254.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.53, default_y=-264.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=174.58):
            with Note(default_x=34.21, default_y=-239.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=107.07, default_y=-219.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=34.21, default_y=-249.18):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=107.07, default_y=-239.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=140.02, default_y=-244.18):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=164.66):
            with Note(default_x=25.14, default_y=-224.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=120.73, default_y=-224.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=25.5, default_y=-249.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=67.83, default_y=-259.18):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.73, default_y=-249.18):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=218.02):
            with Note(default_x=23.13, default_y=-224.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=145.69, default_y=-224.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.13, default_y=-244.18):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=145.69, default_y=-244.18):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=182.47, default_y=-249.18):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=205.2):
            with Note(default_x=20.88, default_y=-244.18):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=152.97, default_y=-229.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.24, default_y=-254.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.54, default_y=-264.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.97, default_y=-254.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=241.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(228.51)
            with Direction(placement='above'):
                with DirectionType():
                    Words('This edition produced by Andrew Sims 2018', default_y=38.5, relative_y=20.0, font_family='Times New Roman')
            with Note(default_x=90.38, default_y=-263.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=190.37, default_y=-268.51):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=90.38, default_y=-283.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=190.37, default_y=-293.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=229.99):
            with Note(default_x=12.61, default_y=-263.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.89, default_y=-268.51):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.16, default_y=-273.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=153.71, default_y=-278.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-288.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.16, default_y=-283.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=118.44, default_y=-288.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.58, default_y=-283.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=193.11, default_y=-293.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=177.38):
            with Note(default_x=17.23, default_y=-278.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=119.28, default_y=-263.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=17.59, default_y=-288.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.78, default_y=-283.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=91.03, default_y=-288.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=119.28, default_y=-293.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=147.53, default_y=-298.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=226.65):
            with Note(default_x=12.61, default_y=-263.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.42, default_y=-248.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.83, default_y=-253.51):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=154.24, default_y=-258.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.61, default_y=-283.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.42, default_y=-293.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=154.24, default_y=-278.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=118.89):
            with Note(default_x=23.13, default_y=-263.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(4.0)
            with Note(default_x=23.13, default_y=-298.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')