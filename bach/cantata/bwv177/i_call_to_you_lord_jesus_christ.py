with ScorePartwise(version='3.1'):
    with Identification():
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-15')
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
        with ScorePart(id='P1'):
            PartName('Midi_1', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Midi_1', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Midi_1', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Midi_1', print_object='no')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=168.45):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(295.2)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-49.35, default_y=56.38, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Sound(tempo=55.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words("Choral, Vers 5: Ich ruf' zu dir, Herr Jesu Christ, BWV 177", default_y=28.2, relative_y=20.0, font_family='Arial', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-49.35, default_y=88.09, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Sound(tempo=55.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-49.35, default_y=119.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Sound(tempo=55.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-49.35, default_y=151.51, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Sound(tempo=55.0)
            with Note(default_x=124.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
        with Measure(number='2', width=321.96):
            with Note(default_x=19.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('lieg')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=89.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('im')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('ner')
            with Note(default_x=123.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=167.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Streit')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=202.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('al')
            with Note(default_x=285.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=308.73):
            with Note(default_x=19.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('wi')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Note(default_x=77.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=99.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ich')
            with Note(default_x=187.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.3, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text("streb',")
                with Lyric(number='2', default_x=11.26, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text("kleb',")
            with Note(default_x=236.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.63, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('hilf,')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=271.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=313.01):
            with Note(default_x=32.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=67.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Johann Sebastian Bach\n', default_y=18.21, relative_y=20.0, font_family='Arial', font_size='12')
                    Words('Text: Johann Agricola')
            with Note(default_x=102.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=137.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=171.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.76, default_y=-55.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ,')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stär')
            with Note(default_x=241.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
                with Lyric(number='2', default_x=6.58, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('ker')
            with Note(default_x=276.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=245.41):
            with Note(default_x=31.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-55.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schwa')
                with Lyric(number='2', default_x=6.94, default_y=-78.72, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma')
            with Note(default_x=155.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.74, default_y=-55.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen;')
                with Lyric(number='2', default_x=9.23, default_y=-78.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='6', width=235.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=141.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kömmt')
        with Measure(number='7', width=310.49):
            with Note(default_x=20.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=90.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
            with Note(default_x=126.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=161.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('fech')
            with Note(default_x=197.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=232.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=9.09, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('tung,')
            with Note(default_x=268.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=296.49):
            with Note(default_x=23.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.78, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=58.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=166.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.21, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text("wehr',")
            with Note(default_x=223.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='9', width=299.16):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=87.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=157.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=227.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('um')
            with Note(default_x=262.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=215.89):
            with Note(default_x=15.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto')
            with Note(default_x=143.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.46, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ße.')
        with Measure(number='11', width=367.71):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=99.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=145.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=223.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
        with Measure(number='12', width=268.08):
            with Note(default_x=23.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.48, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen,')
            with Note(default_x=73.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=141.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text("mir's")
            with Note(default_x=204.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
        with Measure(number='13', width=265.12):
            with Note(default_x=26.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.49, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text("bring'")
            with Note(default_x=88.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Note(default_x=151.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.45, default_y=-47.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('fahr.')
            with Note(default_x=201.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
        with Measure(number='14', width=289.46):
            with Note(default_x=24.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß,')
            with Note(default_x=88.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=152.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text("wirst's")
            with Note(default_x=184.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=216.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=248.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=167.19):
            with Note(default_x=14.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('las')
            with Note(default_x=58.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-47.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('sen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=168.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(121.98)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=124.72, default_y=-186.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
        with Measure(number='2', width=321.96):
            with Note(default_x=19.54, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('lieg')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=89.13, default_y=-196.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('im')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ner')
            with Note(default_x=167.41, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Streit')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=202.2, default_y=-196.98):
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
            with Note(default_x=242.75, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('al')
            with Note(default_x=285.57, default_y=-196.98):
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
        with Measure(number='3', width=308.73):
            with Note(default_x=19.8, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=143.57, default_y=-186.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ich')
            with Note(default_x=187.78, default_y=-196.98):
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
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.3, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text("streb',")
                with Lyric(number='2', default_x=11.26, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text("kleb',")
            with Note(default_x=236.4, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.63, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('hilf,')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
        with Measure(number='4', width=313.01):
            with Note(default_x=32.4, default_y=-196.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=102.15, default_y=-196.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=171.9, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ,')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stär')
            with Note(default_x=241.65, default_y=-196.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ker')
        with Measure(number='5', width=245.41):
            with Note(default_x=31.89, default_y=-201.98):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schwa')
                with Lyric(number='2', default_x=6.58, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma')
            with Note(default_x=62.88, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=124.84, default_y=-196.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=155.83, default_y=-191.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.74, default_y=-55.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen;')
                with Lyric(number='2', default_x=9.23, default_y=-79.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='6', width=235.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.28)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=141.59, default_y=-165.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kömmt')
            with Note(default_x=180.65, default_y=-150.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.52, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=310.49):
            with Note(default_x=20.05, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=90.93, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural', parentheses='yes')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An')
            with Note(default_x=161.81, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fech')
            with Note(default_x=232.69, default_y=-150.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.09, default_y=-50.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('tung,')
        with Measure(number='8', width=296.49):
            with Note(default_x=23.18, default_y=-150.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.78, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=58.93, default_y=-145.28):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.68, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=166.19, default_y=-165.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.21, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text("wehr',")
            with Note(default_x=223.39, default_y=-165.28):
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
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=259.14, default_y=-160.28):
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
        with Measure(number='9', width=299.16):
            with Note(default_x=17.23, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=52.27, default_y=-145.28):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=87.31, default_y=-150.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=122.35, default_y=-155.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=157.39, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=192.44, default_y=-165.28):
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
            with Note(default_x=227.48, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um')
        with Measure(number='10', width=215.89):
            with Note(default_x=15.51, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('sto')
            with Note(default_x=79.63, default_y=-165.28):
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
                    Slur(type='stop', number=1)
            with Note(default_x=143.4, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.46, default_y=-50.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('ße.')
        with Measure(number='11', width=367.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.28)
            with Note(default_x=99.18, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=178.8, default_y=-165.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=223.63, default_y=-165.28):
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
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma')
            with Note(default_x=257.15, default_y=-170.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.11, default_y=-175.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.06, default_y=-170.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=268.08):
            with Note(default_x=23.7, default_y=-180.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.48, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen,')
            with Note(default_x=73.64, default_y=-180.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=141.63, default_y=-165.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text("mir's")
            with Note(default_x=204.05, default_y=-170.28):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=235.27, default_y=-165.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='13', width=265.12):
            with Note(default_x=26.46, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=8.49, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text("bring'")
            with Note(default_x=57.65, default_y=-170.28):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.84, default_y=-180.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Note(default_x=151.23, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.45, default_y=-51.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('fahr.')
            with Note(default_x=201.14, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
        with Measure(number='14', width=289.46):
            with Note(default_x=24.43, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß,')
            with Note(default_x=56.49, default_y=-165.28):
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
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.55, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=120.61, default_y=-155.28):
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
            with Note(default_x=152.67, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text("wirst's")
            with Note(default_x=184.73, default_y=-165.28):
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
            with Note(default_x=216.79, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
        with Measure(number='15', width=167.19):
            with Note(default_x=14.76, default_y=-160.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('las')
            with Note(default_x=58.4, default_y=-165.28):
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
                    Slur(type='stop', number=1)
            with Note(default_x=112.95, default_y=-175.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-51.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('sen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=168.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(124.87)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=124.72, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
        with Measure(number='2', width=321.96):
            with Note(default_x=19.54, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('lieg')
                with Lyric(number='2', default_y=-71.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=54.34, default_y=-331.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=123.92, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('im')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ner')
            with Note(default_x=145.66, default_y=-341.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.05, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Streit')
                with Lyric(number='2', default_x=6.94, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
        with Measure(number='3', width=308.73):
            with Note(default_x=19.8, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.16, default_y=-336.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=99.37, default_y=-341.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('wi')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Note(default_x=121.47, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=143.57, default_y=-351.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=165.67, default_y=-356.84):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=187.78, default_y=-351.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=11.3, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text("streb',")
                with Lyric(number='2', default_x=11.26, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text("kleb',")
            with Note(default_x=236.4, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.63, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('hilf,')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
        with Measure(number='4', width=313.01):
            with Note(default_x=32.4, default_y=-341.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=102.15, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=137.02, default_y=-351.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=171.9, default_y=-356.84):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ,')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stär')
            with Note(default_x=241.65, default_y=-351.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ker')
            with Note(default_x=276.53, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=245.41):
            with Note(default_x=31.89, default_y=-341.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schwa')
                with Lyric(number='2', default_x=6.58, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma')
            with Note(default_x=62.88, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.86, default_y=-351.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=155.83, default_y=-346.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.74, default_y=-47.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen;')
                with Lyric(number='2', default_x=9.23, default_y=-71.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='6', width=235.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.4)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef(after_barline='yes'):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=141.59, default_y=-283.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kömmt')
        with Measure(number='7', width=310.49):
            with Note(default_x=20.05, default_y=-283.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=55.49, default_y=-268.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.93, default_y=-273.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
            with Note(default_x=126.37, default_y=-278.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=161.81, default_y=-273.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fech')
            with Note(default_x=268.12, default_y=-268.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.09, default_y=-53.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('tung,')
        with Measure(number='8', width=296.49):
            with Note(default_x=23.18, default_y=-263.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.78, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=58.93, default_y=-258.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.68, default_y=-263.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=130.44, default_y=-268.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.19, default_y=-273.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.21, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text("wehr',")
            with Note(default_x=223.39, default_y=-283.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='9', width=299.16):
            with Note(default_x=17.23, default_y=-288.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=87.31, default_y=-293.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=157.39, default_y=-278.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=192.44, default_y=-273.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=227.48, default_y=-268.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um')
        with Measure(number='10', width=215.89):
            with Note(default_x=15.51, default_y=-273.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('sto')
            with Note(default_x=47.57, default_y=-278.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.7, default_y=-283.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=143.4, default_y=-283.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.18, default_y=-53.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('ße.')
        with Measure(number='11', width=367.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.63)
            with Note(default_x=99.18, default_y=-281.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=145.27, default_y=-281.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=223.63, default_y=-276.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma')
            with Note(default_x=299.06, default_y=-281.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=332.58, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=268.08):
            with Note(default_x=23.7, default_y=-291.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=9.48, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen,')
            with Note(default_x=73.64, default_y=-291.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=141.63, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text("mir's")
            with Note(default_x=172.84, default_y=-291.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=204.05, default_y=-296.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=235.27, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=265.12):
            with Note(default_x=26.46, default_y=-271.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.49, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text("bring'")
            with Note(default_x=57.65, default_y=-261.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.84, default_y=-261.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ge')
            with Note(default_x=120.04, default_y=-266.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=151.23, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.45, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('fahr.')
            with Note(default_x=201.14, default_y=-281.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
            with Note(default_x=232.33, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=289.46):
            with Note(default_x=24.43, default_y=-291.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß,')
            with Note(default_x=88.55, default_y=-296.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=120.61, default_y=-276.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=152.67, default_y=-276.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text("wirst's")
            with Note(default_x=248.85, default_y=-271.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
        with Measure(number='15', width=167.19):
            with Note(default_x=14.76, default_y=-276.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('las')
            with Note(default_x=85.68, default_y=-281.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.95, default_y=-286.91):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-58.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('sen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=168.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(114.62)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=124.72, default_y=-491.46):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('An')
        with Measure(number='2', width=321.96):
            with Note(default_x=19.18, default_y=-486.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('lieg')
                with Lyric(number='2', default_y=-71.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=167.41, default_y=-486.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=202.2, default_y=-481.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('im')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('ner')
            with Note(default_x=242.75, default_y=-476.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Streit')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=285.57, default_y=-481.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
        with Measure(number='3', width=308.73):
            with Note(default_x=19.8, default_y=-486.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('wi')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('lein')
            with Note(default_x=55.16, default_y=-491.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.37, default_y=-496.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('ich')
            with Note(default_x=187.78, default_y=-501.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.3, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text("streb',")
                with Lyric(number='2', default_x=11.26, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text("kleb',")
            with Note(default_x=236.4, default_y=-486.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.63, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('hilf,')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
        with Measure(number='4', width=313.01):
            with Note(default_x=32.4, default_y=-481.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=102.15, default_y=-476.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=171.9, default_y=-496.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.76, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ,')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('stär')
            with Note(default_x=206.78, default_y=-491.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=241.65, default_y=-496.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
                with Lyric(number='2', default_x=6.58, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('ker')
            with Note(default_x=276.53, default_y=-501.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=245.41):
            with Note(default_x=31.53, default_y=-506.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schwa')
                with Lyric(number='2', default_x=6.22, default_y=-71.15, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ma')
            with Note(default_x=155.83, default_y=-521.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.74, default_y=-47.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen;')
                with Lyric(number='2', default_x=9.23, default_y=-71.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='6', width=235.53):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.87)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=141.59, default_y=-420.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kömmt')
        with Measure(number='7', width=310.49):
            with Note(default_x=20.05, default_y=-415.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
            with Note(default_x=90.93, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An')
            with Note(default_x=161.81, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fech')
            with Note(default_x=232.69, default_y=-405.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.09, default_y=-46.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('tung,')
        with Measure(number='8', width=296.49):
            with Note(default_x=23.18, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.78, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr,')
            with Note(default_x=58.93, default_y=-415.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.68, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=166.19, default_y=-430.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=11.21, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text("wehr',")
            with Note(default_x=223.39, default_y=-395.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='9', width=299.16):
            with Note(default_x=17.23, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=87.31, default_y=-405.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=122.35, default_y=-410.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=157.39, default_y=-415.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=227.48, default_y=-420.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('um')
            with Note(default_x=262.52, default_y=-425.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=215.89):
            with Note(default_x=15.15, default_y=-420.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto')
            with Note(default_x=143.4, default_y=-415.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.18, default_y=-46.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ße.')
        with Measure(number='11', width=367.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(125.77)
            with Note(default_x=99.18, default_y=-447.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=145.27, default_y=-442.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
            with Note(default_x=223.63, default_y=-462.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma')
            with Note(default_x=299.06, default_y=-457.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=268.08):
            with Note(default_x=23.7, default_y=-442.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.48, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('chen,')
            with Note(default_x=73.64, default_y=-442.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
            with Note(default_x=110.42, default_y=-447.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.63, default_y=-452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text("mir's")
            with Note(default_x=204.05, default_y=-447.68):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=235.27, default_y=-452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=265.12):
            with Direction(placement='above'):
                with DirectionType():
                    Words('© 2011 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded. Edited by Juliane Claudi ', default_y=14.39, relative_y=20.0, font_family='Arial', font_size='9')
            with Note(default_x=26.46, default_y=-457.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.49, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text("bring'")
            with Note(default_x=57.65, default_y=-462.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.84, default_y=-467.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Note(default_x=151.23, default_y=-472.68):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.45, default_y=-47.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('fahr.')
            with Note(default_x=201.14, default_y=-457.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich')
        with Measure(number='14', width=289.46):
            with Note(default_x=24.43, default_y=-452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß,')
            with Note(default_x=88.55, default_y=-447.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=120.61, default_y=-442.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=152.67, default_y=-437.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text("wirst's")
            with Note(default_x=184.73, default_y=-432.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=216.79, default_y=-427.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
            with Note(default_x=248.85, default_y=-422.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=167.19):
            with Note(default_x=14.76, default_y=-417.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('las')
            with Note(default_x=58.4, default_y=-452.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.95, default_y=-437.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-47.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('sen.')
            with Barline(location='right'):
                BarStyle('light-heavy')