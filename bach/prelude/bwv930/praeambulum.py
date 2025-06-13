with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('(Prelude) BWV 930')
        WorkTitle('Praeambulum')
    with Identification():
        Creator('Johann Sebastian Bach', type='composer')
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
        CreditWords('Praeambulum', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(Prelude) BWV 930', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName(None)
            with ScoreInstrument(id='P1-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName(None)
            with ScoreInstrument(id='P2-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName(None)
            with ScoreInstrument(id='P3-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName(None)
            with ScoreInstrument(id='P4-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=235.71):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('minor')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=131.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=151.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=171.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=191.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=210.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=134.28):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=134.28):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=161.99):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=134.16):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=29.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=49.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=69.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=89.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=109.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='6', width=134.16):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=29.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=49.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=69.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=89.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=109.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='7', width=142.9):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=31.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=52.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=75.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=96.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=118.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='8', width=259.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=102.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=127.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=151.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=181.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=206.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=233.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='9', width=158.0):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=39.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=61.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=84.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=106.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=133.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='10', width=145.35):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=37.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=58.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=79.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=99.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=120.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='11', width=184.35):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=161.5):
            with Note(default_x=16.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='13', width=168.75):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=60.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=142.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='14', width=257.64):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=90.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='15', width=153.88):
            with Note(default_x=10.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=84.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=129.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='16', width=189.65):
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=166.43):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=75.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=97.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=119.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=141.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=173.31):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=68.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=98.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=136.58):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=261.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(138.94)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=165.69):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=172.46):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=163.72):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=146.34):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=168.09):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=253.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(138.94)
            with Note(default_x=99.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=123.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=152.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=177.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=202.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=226.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='27', width=161.45):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=34.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=59.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=83.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=108.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=135.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='28', width=161.34):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=167.09):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=38.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=66.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=91.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=116.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=140.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='30', width=185.66):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=144.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=148.8):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=55.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=78.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=101.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=124.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='32', width=257.72):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=156.86):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='34', width=188.17):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=155.36):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='36', width=164.03):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=155.36):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=39.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=62.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=85.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=107.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=130.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='38', width=312.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=94.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=130.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=166.44, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=202.57, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=238.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='39', width=201.69):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=82.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=115.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=147.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5/1')
        with Measure(number='40', width=190.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=41.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=73.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=155.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='41', width=242.43):
            with Note(default_x=10.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=202.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='42', width=130.58):
            with Note(default_x=17.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=235.71):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(76.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('minor')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=134.28):
            with Note(default_x=10.12, default_y=-126.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=134.28):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=30.0, default_y=-126.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=49.88, default_y=-136.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=69.76, default_y=-146.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=89.64, default_y=-111.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=109.51, default_y=-136.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='4', width=161.99):
            with Note(default_x=10.0, default_y=-141.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=33.72, default_y=-111.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=57.43, default_y=-116.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=84.1, default_y=-121.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=107.81, default_y=-116.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=136.68, default_y=-141.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='5', width=134.16):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=134.16):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=142.9):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=259.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=158.0):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=145.35):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=184.35):
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=26.61, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=43.22, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=76.44, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Ornaments():
                        Mordent()
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=156.17, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='12', width=161.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=39.47, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=61.93, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=91.82, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=114.28, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='13', width=168.75):
            with Note(default_x=10.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=35.69, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=60.66, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=87.32, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=117.22, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='14', width=257.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=143.96, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=176.21, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=176.21, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='15', width=153.88):
            with Note(default_x=10.94, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=33.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=62.9, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=107.05, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=107.05, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=189.65):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=33.67, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.18, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.18, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=111.61, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=111.61, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.61, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=166.43):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=173.31):
            with Note(default_x=14.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='19', width=136.58):
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.36, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=50.73, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=71.09, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=91.45, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=111.81, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=261.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=99.18, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=152.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=179.38, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=206.12, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=232.85, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=165.69):
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=37.33, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=60.85, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=84.38, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=117.04, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=140.57, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='22', width=172.46):
            with Note(default_x=16.2, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=48.87, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=73.26, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=97.66, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=122.06, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=146.46, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='23', width=163.72):
            with Note(default_x=16.2, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=39.61, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=63.02, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=91.89, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=115.3, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=138.71, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='24', width=146.34):
            with Note(default_x=14.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=35.52, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=57.03, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=78.55, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.06, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=121.58, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='25', width=168.09):
            with Note(default_x=16.2, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=39.73, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=63.25, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=86.78, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=119.44, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=142.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='26', width=253.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=161.45):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='28', width=161.34):
            with Note(default_x=13.8, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=167.09):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=185.66):
            with Note(default_x=16.2, default_y=-126.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=68.39, default_y=-126.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='31', width=148.8):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=257.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.2)
            with Note(default_x=101.58, default_y=-111.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=147.87, default_y=-111.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=217.29, default_y=-116.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.96, default_y=-111.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=156.86):
            with Note(default_x=10.0, default_y=-116.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.21, default_y=-126.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=58.42, default_y=-116.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=82.63, default_y=-106.2):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=106.84, default_y=-91.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=131.05, default_y=-96.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='34', width=188.17):
            with Note(default_x=16.2, default_y=-101.2):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=46.1, default_y=-106.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=74.19, default_y=-101.2):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=102.29, default_y=-91.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=130.38, default_y=-96.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=158.48, default_y=-101.2):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
        with Measure(number='35', width=155.36):
            with Note(default_x=17.23, default_y=-106.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=39.9, default_y=-96.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=62.57, default_y=-106.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=85.25, default_y=-116.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=107.92, default_y=-96.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=130.59, default_y=-121.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='36', width=164.03):
            with Note(default_x=10.72, default_y=-126.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=35.29, default_y=-116.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=59.86, default_y=-126.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=84.42, default_y=-136.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=113.29, default_y=-111.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=137.86, default_y=-136.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-59.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='37', width=155.36):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='38', width=312.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.55)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=201.69):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.89, default_y=-199.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=82.54, default_y=-199.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=82.54, default_y=-179.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.85, default_y=-199.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=147.85, default_y=-184.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='40', width=190.23):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=73.12, default_y=-189.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-60.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='41', width=242.43):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.25, default_y=-199.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=87.57, default_y=-194.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-60.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=125.88, default_y=-204.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-60.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=125.88, default_y=-194.55):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=164.2, default_y=-214.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=164.2, default_y=-204.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=164.2, default_y=-194.55):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='42', width=130.58):
            with Note(default_x=17.44, default_y=-209.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=17.44, default_y=-199.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P3'):
        with Measure(number='1', width=235.71):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(102.78)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('minor')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=134.28):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=30.0, default_y=-298.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=49.88, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=69.76, default_y=-278.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=89.64, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=109.51, default_y=-298.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=134.28):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.88, default_y=-298.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=69.76, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=89.64, default_y=-278.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=109.51, default_y=-263.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='4', width=161.99):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=134.16):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.76, default_y=-308.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=69.64, default_y=-298.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=89.52, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=109.4, default_y=-273.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='6', width=134.16):
            with Note(default_x=10.0, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=89.52, default_y=-288.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=142.9):
            with Note(default_x=10.0, default_y=-283.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=52.44, default_y=-318.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=75.7, default_y=-308.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=96.92, default_y=-298.78):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=118.14, default_y=-283.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='8', width=259.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.4)
            with Note(default_x=102.42, default_y=-282.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='9', width=158.0):
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=39.56, default_y=-292.4):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.56, default_y=-262.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=145.35):
            with Note(default_x=17.23, default_y=-267.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=184.35):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=103.02, default_y=-247.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=129.6, default_y=-242.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=156.17, default_y=-237.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
        with Measure(number='12', width=161.5):
            with Note(default_x=16.66, default_y=-232.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=114.28, default_y=-232.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=136.73, default_y=-232.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=168.75):
            with Note(default_x=10.36, default_y=-237.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Ornaments():
                        Mordent()
        with Measure(number='14', width=257.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=90.38, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=202.82, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=229.43, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='15', width=153.88):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.9, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=107.05, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='16', width=189.65):
            with Note(default_x=10.36, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=166.43):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=75.45, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=173.31):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='19', width=136.58):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=50.73, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=261.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=165.69):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=60.85, default_y=-246.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=172.46):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=163.72):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=146.34):
            with Note(default_x=14.0, default_y=-251.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=100.06, default_y=-246.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='25', width=168.09):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=253.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=202.15, default_y=-241.2):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='27', width=161.45):
            with Note(default_x=10.0, default_y=-236.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=59.27, default_y=-261.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=108.55, default_y=-251.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='28', width=161.34):
            with Note(default_x=13.8, default_y=-271.2):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=38.12, default_y=-261.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=62.45, default_y=-251.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=86.77, default_y=-236.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=111.09, default_y=-251.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=135.42, default_y=-261.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
        with Measure(number='29', width=167.09):
            with Note(default_x=13.8, default_y=-271.2):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=185.66):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=148.8):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=55.61, default_y=-256.2):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=257.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.35)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=156.86):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=58.42, default_y=-261.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='34', width=188.17):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=74.19, default_y=-251.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=130.38, default_y=-256.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='35', width=155.36):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.57, default_y=-246.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=107.92, default_y=-241.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
        with Measure(number='36', width=164.03):
            with Note(default_x=10.72, default_y=-236.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=59.86, default_y=-231.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=113.29, default_y=-226.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='37', width=155.36):
            with Note(default_x=17.23, default_y=-231.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=62.57, default_y=-236.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=107.92, default_y=-241.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
        with Measure(number='38', width=312.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.2)
            with Note(default_x=94.18, default_y=-275.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=130.31, default_y=-290.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=166.44, default_y=-300.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=202.57, default_y=-310.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=238.7, default_y=-285.75):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=274.83, default_y=-310.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='39', width=201.69):
            with Note(default_x=16.87, default_y=-315.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Ornaments():
                        Mordent()
            with Note(default_x=147.85, default_y=-310.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='40', width=190.23):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=124.18, default_y=-325.75):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='41', width=242.43):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.57, default_y=-295.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=164.2, default_y=-295.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=164.2, default_y=-285.75):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=130.58):
            with Note(default_x=17.44, default_y=-290.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('1/2')
            with Note(default_x=17.44, default_y=-275.75):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P4'):
        with Measure(number='1', width=235.71):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(76.6)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('minor')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='2', width=134.28):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=134.28):
            with Note(default_x=10.12, default_y=-380.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=161.99):
            with Note(default_x=10.0, default_y=-395.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=57.43, default_y=-360.38):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.81, default_y=-395.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=134.16):
            with Note(default_x=10.0, default_y=-390.38):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=134.16):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.76, default_y=-370.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=142.9):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=259.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=151.9, default_y=-352.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=233.21, default_y=-357.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='9', width=158.0):
            with Note(default_x=17.23, default_y=-362.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=145.35):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=58.57, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=120.58, default_y=-342.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
        with Measure(number='11', width=184.35):
            with Note(default_x=10.0, default_y=-347.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=43.22, default_y=-352.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=76.08, default_y=-357.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='12', width=161.5):
            with Note(default_x=16.66, default_y=-362.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('2/5')
        with Measure(number='13', width=168.75):
            with Note(default_x=10.36, default_y=-362.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='14', width=257.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.6)
            with Note(default_x=90.38, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='15', width=153.88):
            with Note(default_x=10.58, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='16', width=189.65):
            with Note(default_x=10.36, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=134.56, default_y=-376.6):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=166.43):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=23.48, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=173.31):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=38.48, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=68.38, default_y=-331.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=98.27, default_y=-321.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=122.75, default_y=-331.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=147.23, default_y=-341.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='19', width=136.58):
            with Note(default_x=10.0, default_y=-326.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=261.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=125.91, default_y=-331.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=152.65, default_y=-321.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=179.38, default_y=-311.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=206.12, default_y=-321.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=232.85, default_y=-331.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='21', width=165.69):
            with Note(default_x=13.8, default_y=-316.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=117.04, default_y=-316.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=172.46):
            with Note(default_x=16.2, default_y=-346.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=73.26, default_y=-321.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=122.06, default_y=-341.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='23', width=163.72):
            with Note(default_x=16.2, default_y=-336.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=39.61, default_y=-331.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=63.02, default_y=-336.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=91.89, default_y=-341.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=115.3, default_y=-346.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=138.71, default_y=-351.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='24', width=146.34):
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=57.03, default_y=-331.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=168.09):
            with Note(default_x=16.2, default_y=-326.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=119.44, default_y=-336.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='26', width=253.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.6)
            with Note(default_x=99.18, default_y=-332.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=152.75, default_y=-347.8):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=161.45):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='28', width=161.34):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=167.09):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=185.66):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=41.72, default_y=-352.8):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=68.39, default_y=-342.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=93.91, default_y=-332.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=119.43, default_y=-342.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=144.95, default_y=-352.8):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='31', width=148.8):
            with Note(default_x=10.0, default_y=-337.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
                with Lyric(number='1', default_x=6.58, default_y=-49.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='32', width=257.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=124.73, default_y=-346.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
            with Note(default_x=147.87, default_y=-336.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=171.01, default_y=-326.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(default_x=194.15, default_y=-336.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=217.29, default_y=-346.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('4')
        with Measure(number='33', width=156.86):
            with Note(default_x=10.0, default_y=-331.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('1')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=106.84, default_y=-356.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
        with Measure(number='34', width=188.17):
            with Note(default_x=16.2, default_y=-351.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='35', width=155.36):
            with Note(default_x=16.87, default_y=-356.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
        with Measure(number='36', width=164.03):
            with Note(default_x=10.36, default_y=-356.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='37', width=155.36):
            with Note(default_x=16.87, default_y=-356.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='38', width=312.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=201.69):
            with Note(print_object='no'):
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='40', width=190.23):
            with Note(default_x=10.12, default_y=-400.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=73.48, default_y=-395.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='41', width=242.43):
            with Note(default_x=10.58, default_y=-415.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='42', width=130.58):
            with Note(default_x=17.44, default_y=-415.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')