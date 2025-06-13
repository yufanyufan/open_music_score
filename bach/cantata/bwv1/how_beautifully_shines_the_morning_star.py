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
    with PartList():
        with ScorePart(id='P1'):
            PartName('1.Cantus G2')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('II. Cantus C1')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P2-I1', port=2)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Altus C3')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P3-I1', port=3)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Tenor C4')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P4-I1', port=4)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Bassus F4')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P5-I1', port=5)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Cantus C1')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P6-I1', port=6)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Altus  C3')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P7-I1', port=7)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Tenor C4')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P8-I1', port=8)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Bassus F4')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P9-I1', port=9)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P10'):
            PartName('Bassus  generalis')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P10-I1', port=10)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(2)
                MidiProgram(33)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=507.13):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(169.6)
                        RightMargin(0.0)
                    TopSystemDistance(422.2)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Sound(tempo=160.0)
            with Note(default_x=105.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=189.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=295.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
            with Note(default_x=347.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=452.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='2', width=400.76):
            with Note(default_x=22.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=67.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=123.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=10.54, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=281.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=309.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=336.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=205.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
            with Note(default_x=329.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=454.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=578.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
            with Note(default_x=702.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=827.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=951.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Note(default_x=80.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=178.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=236.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.2, default_y=-47.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
        with Measure(number='5', width=291.8):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=83.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-47.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=116.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=136.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=157.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note(default_x=223.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
        with Measure(number='6', width=181.87):
            with Note(default_x=16.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
            with Note(default_x=72.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=114.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.75, default_y=-47.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-26.67, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Note(default_x=28.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-47.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.08, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Note(default_x=80.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=16.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=163.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=216.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-32.2, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Note(default_x=32.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.17, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
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
            with Note(default_x=195.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=249.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=357.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=81.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=198.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=315.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=432.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=505.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=578.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=724.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=841.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=958.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Note(default_x=80.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-48.08, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Note(default_x=49.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=89.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.99, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Note(default_x=80.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=16.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=140.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=184.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-30.63, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Note(default_x=32.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=682.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=944.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=268.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=328.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
        with Measure(number='38', width=493.75):
            with Note(default_x=28.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=84.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=196.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=266.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=379.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.09, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=682.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=944.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Note(default_x=83.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=159.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=240.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=278.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=316.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='41', width=220.26):
            with Note(default_x=19.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=53.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=87.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=139.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-28.24, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='43', width=237.42):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=691.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=183.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='46', width=304.41):
            with Note(default_x=27.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=80.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=130.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=215.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='47', width=286.14):
            with Note(default_x=25.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=75.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=121.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=201.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='48', width=235.56):
            with Note(default_x=21.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=84.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=146.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-69.08, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Note(default_x=134.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=197.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=323.45, default_y=-15.0):
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
            with Note(default_x=386.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=575.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=69.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=123.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=198.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=253.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=326.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=381.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=565.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=83.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.38, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=198.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=314.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=371.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=443.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=501.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=537.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='53', width=502.73):
            with Note(default_x=27.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-47.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=81.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=148.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=202.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=323.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=393.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=447.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=83.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=200.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=316.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=579.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-45.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=769.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=842.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=959.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=83.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=220.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=456.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=516.92, default_y=-15.0):
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
        with Measure(number='56', width=482.97):
            with Note(default_x=27.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=77.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=126.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=245.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=307.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=372.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(322.2)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=31.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=62.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=93.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=124.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=155.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=186.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=217.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=248.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.24, default_y=279.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('560')
                Sound(tempo=560.0)
            with Note(default_x=98.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('reIch')
            with Note(default_x=106.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=83.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=119.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=154.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=190.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=142.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=86.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=3.73, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(71.25)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
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
            with Note(default_x=242.68, default_y=-146.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=295.25, default_y=-126.25):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=347.82, default_y=-136.25):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
            with Note(default_x=400.03, default_y=-146.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
        with Measure(number='2', width=400.76):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.23, default_y=-131.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=123.49, default_y=-136.25):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=151.62, default_y=-131.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.75, default_y=-126.25):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=207.88, default_y=-136.25):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=235.65, default_y=-121.25):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=336.92, default_y=-121.25):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.95, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.54, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=454.28, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
            with Note(default_x=578.6, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=702.93, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=827.25, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
            with Note(default_x=951.57, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.62)
            with Note(default_x=80.38, default_y=-120.62):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=178.97, default_y=-120.62):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
            with Note(default_x=236.26, default_y=-125.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.2, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
        with Measure(number='5', width=291.8):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.95, default_y=-125.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=83.09, default_y=-120.62):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=116.23, default_y=-125.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note(default_x=157.29, default_y=-130.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=223.57, default_y=-135.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='6', width=181.87):
            with Note(default_x=13.32, default_y=-140.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=114.88, default_y=-135.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.75, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-135.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-140.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-145.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=84.91, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=138.07, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=188.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.86, default_y=-44.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=273.31, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=108.32, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-44.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
            with Note(default_x=112.92, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=154.27, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=4.99, default_y=-44.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=16.47, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=163.53, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=216.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.17, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
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
            with Note(default_x=412.52, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.32, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=198.32, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=315.33, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=432.34, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=578.6, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=651.74, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=724.51, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=958.88, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.56, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=173.12, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=208.29, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=265.13, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='23', width=234.77):
            with Note(default_x=24.06, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=86.16, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=128.32, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
        with Measure(number='24', width=111.9):
            with Note(default_x=13.32, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.15, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.95)
            with Note(default_x=89.18, default_y=-152.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-137.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-147.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.44, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-142.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-132.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-132.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-122.95):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-122.95):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-127.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-127.95):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-122.95):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.99, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=16.47, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=140.65, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=184.32, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=813.65, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.74, default_y=-121.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=143.41, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=205.73, default_y=-121.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=394.11, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=456.79, default_y=-121.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=519.46, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='38', width=493.75):
            with Note(default_x=28.22, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=84.45, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=140.69, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=196.92, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=267.22, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=323.45, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=379.68, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=435.92, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=211.68, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=342.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
            with Note(default_x=548.81, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.25)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.6, default_y=-110.25):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=198.49, default_y=-125.25):
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
            with Note(default_x=240.34, default_y=-120.25):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=316.87, default_y=-125.25):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
        with Measure(number='41', width=220.26):
            with Note(default_x=19.18, default_y=-130.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=53.57, default_y=-135.25):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=87.6, default_y=-140.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=139.67, default_y=-135.25):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-150.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-155.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-150.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=691.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=183.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='46', width=304.41):
            with Note(default_x=27.86, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=80.66, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=130.51, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=215.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='47', width=286.14):
            with Note(default_x=25.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=75.05, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=121.88, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=201.55, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='48', width=235.56):
            with Note(default_x=21.9, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=84.04, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=146.19, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.9)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=134.46, default_y=-135.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=197.1, default_y=-135.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=323.45, default_y=-140.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=386.09, default_y=-145.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=575.44, default_y=-145.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-140.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=69.29, default_y=-125.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=123.41, default_y=-125.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=198.68, default_y=-125.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.02, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=252.79, default_y=-110.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-125.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=83.34, default_y=-116.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=452.23, default_y=-121.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=565.62, default_y=-126.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-131.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-136.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.55)
            with Note(default_x=80.38, default_y=-137.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=6.7, default_y=-49.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=443.24, default_y=-112.55):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-49.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
        with Measure(number='53', width=502.73):
            with Note(default_x=27.82, default_y=-127.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=81.58, default_y=-122.55):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=148.78, default_y=-127.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=202.55, default_y=-132.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=236.15, default_y=-137.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=269.39, default_y=-142.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-49.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=393.24, default_y=-127.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.38, default_y=-49.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.35)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=316.8, default_y=-124.35):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=579.8, default_y=-134.35):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=696.52, default_y=-129.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.02, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=842.44, default_y=-134.35):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=959.16, default_y=-139.35):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.9)
            with Note(default_x=83.7, default_y=-145.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-50.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=159.34, default_y=-145.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=296.51, default_y=-150.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=334.51, default_y=-155.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=372.15, default_y=-150.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=456.11, default_y=-145.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=554.92, default_y=-160.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='56', width=482.97):
            with Note(default_x=27.46, default_y=-140.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=126.93, default_y=-140.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=245.42, default_y=-150.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=307.23, default_y=-155.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=372.67, default_y=-150.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-50.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('rech')
            with Note(default_x=106.92, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.15)
            with Note(default_x=80.38, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-152.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-132.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-147.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-152.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-51.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=142.02, default_y=-147.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-51.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=86.48, default_y=-147.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-142.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=3.73, default_y=-51.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(67.3)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.12)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note(default_x=16.46, default_y=-217.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=83.09, default_y=-237.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=116.23, default_y=-232.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note(default_x=157.65, default_y=-227.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=190.79, default_y=-222.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=223.93, default_y=-217.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=257.06, default_y=-252.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='6', width=181.87):
            with Note(default_x=13.32, default_y=-232.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=114.88, default_y=-252.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.75, default_y=-45.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-232.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-232.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-232.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.58)
            with Note(default_x=80.38, default_y=-232.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-232.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-227.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.08, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-227.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-212.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-207.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-222.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-227.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-222.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-222.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-217.58):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=16.47, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=108.11, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=163.53, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=216.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=36.84, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.71, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=156.69, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=202.29, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=294.57, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
            with Note(default_x=340.53, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.6, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
            with Note(default_x=334.46, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=461.33, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
            with Note(default_x=588.19, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=10.33, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=742.88, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=822.17, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=949.03, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=147.59, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=214.79, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=282.0, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
            with Note(default_x=349.21, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=10.2, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb/')
            with Note(default_x=431.16, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=473.16, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=540.37, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
        with Measure(number='20', width=468.32):
            with Note(default_x=19.62, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=73.81, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=128.01, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=161.88, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=195.39, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=304.14, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
            with Note(default_x=357.97, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.46, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.52)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=198.32, default_y=-227.52):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=315.33, default_y=-222.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=432.34, default_y=-217.52):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=578.6, default_y=-212.52):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=724.87, default_y=-217.52):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=841.88, default_y=-222.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=958.88, default_y=-222.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.63)
            with Note(default_x=80.38, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.56, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=173.12, default_y=-213.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=208.29, default_y=-213.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=301.03, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='23', width=234.77):
            with Note(default_x=24.42, default_y=-223.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=58.32, default_y=-218.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=83.2, default_y=-213.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=176.76, default_y=-218.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=204.96, default_y=-223.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=111.9):
            with Note(default_x=13.32, default_y=-218.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=60.15, default_y=-213.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.41, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-233.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-228.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.0)
            with Note(default_x=89.18, default_y=-243.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                Accidental('natural')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-243.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-238.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-238.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-223.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-228.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-213.95):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-218.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-218.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-218.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-228.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.99, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=14.89, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=35.27, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.45, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=173.58, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=280.34, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=334.39, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=387.59, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=342.26, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=551.77, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=813.65, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.09, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.2)
            with Note(default_x=80.74, default_y=-231.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=143.41, default_y=-226.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=205.73, default_y=-221.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=394.11, default_y=-216.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=456.43, default_y=-211.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='38', width=493.75):
            with Note(default_x=27.86, default_y=-231.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=196.92, default_y=-226.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=267.22, default_y=-221.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=323.09, default_y=-216.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.09, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=435.92, default_y=-221.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.68, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=342.26, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
            with Note(default_x=552.13, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.02, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=683.07, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=813.65, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.7)
            with Note(default_x=83.34, default_y=-217.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=198.49, default_y=-217.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=240.34, default_y=-237.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.44, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig/')
            with Note(default_x=316.87, default_y=-232.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
        with Measure(number='41', width=220.26):
            with Note(default_x=19.18, default_y=-227.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=53.57, default_y=-217.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=87.6, default_y=-232.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=139.67, default_y=-217.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.34, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-232.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-242.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-232.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-242.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=691.57, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.47)
            with Note(default_x=80.38, default_y=-221.47):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=183.19, default_y=-231.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='46', width=304.41):
            with Note(default_x=27.86, default_y=-226.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=80.66, default_y=-216.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=130.51, default_y=-221.47):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=215.0, default_y=-231.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='47', width=286.14):
            with Note(default_x=25.26, default_y=-231.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=75.05, default_y=-231.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=121.88, default_y=-236.47):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=201.55, default_y=-231.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=134.46, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=197.46, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=260.1, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=386.09, default_y=-252.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=512.08, default_y=-237.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-237.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.29, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=123.41, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=198.68, default_y=-242.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=287.2, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=326.9, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=381.38, default_y=-232.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=83.34, default_y=-248.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.47, default_y=-233.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-228.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-228.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.2)
            with Note(default_x=83.34, default_y=-244.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.38, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=313.68, default_y=-229.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=443.6, default_y=-244.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=501.19, default_y=-239.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='53', width=502.73):
            with Note(default_x=27.82, default_y=-244.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=81.58, default_y=-249.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=115.18, default_y=-249.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=148.78, default_y=-254.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-47.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=202.55, default_y=-249.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=269.75, default_y=-244.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=357.12, default_y=-239.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=393.6, default_y=-234.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=447.36, default_y=-229.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.65)
            with Note(default_x=83.7, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.43, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=10.02, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
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
            with Note(default_x=696.52, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=842.44, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=959.16, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.35)
            with Note(default_x=83.7, default_y=-250.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=159.7, default_y=-260.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=258.51, default_y=-255.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=296.51, default_y=-250.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=334.51, default_y=-245.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=372.15, default_y=-240.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=456.11, default_y=-235.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=516.92, default_y=-250.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='56', width=482.97):
            with Note(default_x=27.82, default_y=-245.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.56, default_y=-240.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.93, default_y=-235.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=245.42, default_y=-240.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=307.23, default_y=-245.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
            with Note(default_x=372.67, default_y=-240.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.34, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.82)
            with Note(default_x=80.38, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-230.82):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-220.82):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-240.82):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-225.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('rech')
            with Note(default_x=147.4, default_y=-235.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-230.82):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.92, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.2)
            with Note(default_x=80.38, default_y=-253.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-238.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-228.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=68.95, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.92, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=86.48, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-233.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=13.52, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-357.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-352.74):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-347.74):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-352.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-352.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-342.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.29, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-342.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-352.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-332.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-352.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-332.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-337.58):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-337.58):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-332.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.5)
            with Note(default_x=80.38, default_y=-351.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-341.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=14.89, default_y=-331.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=11.48, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=33.88, default_y=-331.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.39, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=248.61, default_y=-351.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=294.57, default_y=-331.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=340.53, default_y=-341.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.65)
            with Note(default_x=80.38, default_y=-354.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.53, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid/')
            with Note(default_x=461.33, default_y=-339.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=587.83, default_y=-344.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=822.17, default_y=-354.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
            with Note(default_x=949.03, default_y=-349.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.65)
            with Note(default_x=80.38, default_y=-354.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.59, default_y=-349.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
            with Note(default_x=214.79, default_y=-344.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=282.0, default_y=-344.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
            with Note(default_x=348.85, default_y=-349.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.97, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=540.37, default_y=-354.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='20', width=468.32):
            with Note(default_x=19.62, default_y=-359.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=73.81, default_y=-354.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=128.01, default_y=-349.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=195.75, default_y=-354.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=249.94, default_y=-349.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=304.14, default_y=-359.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
            with Note(default_x=357.97, default_y=-354.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.83, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb/')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=137.23, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=208.29, default_y=-338.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=265.13, default_y=-343.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='23', width=234.77):
            with Note(default_x=24.06, default_y=-348.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=86.16, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=128.32, default_y=-333.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
        with Measure(number='24', width=111.9):
            with Note(default_x=13.32, default_y=-333.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.15, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-343.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-353.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-368.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=89.18, default_y=-358.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-358.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-358.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.44, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-353.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-338.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-343.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-343.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-343.95):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-338.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-358.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-358.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.2, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.38, default_y=-351.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-351.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=16.47, default_y=-346.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=140.65, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=184.32, default_y=-346.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-351.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note(default_x=226.78, default_y=-331.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=334.39, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=387.59, default_y=-331.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.74, default_y=-331.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.68, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=342.26, default_y=-336.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=551.77, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=814.01, default_y=-346.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=944.95, default_y=-346.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-346.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=143.41, default_y=-346.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=206.09, default_y=-351.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=268.76, default_y=-351.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=331.44, default_y=-346.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=394.11, default_y=-346.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=456.43, default_y=-351.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='38', width=493.75):
            with Note(default_x=28.22, default_y=-356.1):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=84.09, default_y=-321.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=196.92, default_y=-326.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=232.07, default_y=-331.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=266.85, default_y=-336.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=379.32, default_y=-336.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.74, default_y=-331.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.68, default_y=-331.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=342.26, default_y=-346.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=551.77, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=944.95, default_y=-341.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.25)
            with Note(default_x=83.7, default_y=-353.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.96, default_y=-348.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=159.87, default_y=-353.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-358.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-363.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-358.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-363.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=691.57, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-336.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=183.19, default_y=-356.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note(default_x=25.26, default_y=-356.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=75.05, default_y=-356.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=121.88, default_y=-351.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=201.55, default_y=-336.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='48', width=235.56):
            with Note(default_x=21.9, default_y=-331.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=84.04, default_y=-321.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=146.19, default_y=-336.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.65)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=134.46, default_y=-367.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-51.97, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=197.46, default_y=-357.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=260.46, default_y=-367.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=323.45, default_y=-362.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=386.09, default_y=-357.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.97, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=512.08, default_y=-377.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.22, default_y=-51.97, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-377.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.29, default_y=-367.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=123.41, default_y=-372.45):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-51.97, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=198.68, default_y=-367.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-51.97, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=253.15, default_y=-357.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=326.9, default_y=-367.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=381.38, default_y=-362.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.65)
            with Note(default_x=83.34, default_y=-353.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.47, default_y=-373.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-363.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-368.45):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.25, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=83.7, default_y=-375.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=141.28, default_y=-340.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=198.87, default_y=-355.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=256.45, default_y=-350.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=314.04, default_y=-355.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=371.62, default_y=-360.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=407.61, default_y=-360.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=443.6, default_y=-365.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-47.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=501.19, default_y=-360.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='53', width=502.73):
            with Note(default_x=27.82, default_y=-355.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.58, default_y=-375.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-47.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=269.75, default_y=-380.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=357.12, default_y=-375.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=393.6, default_y=-370.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr/')
            with Note(default_x=447.36, default_y=-355.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.65)
            with Note(default_x=83.7, default_y=-360.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=200.43, default_y=-355.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=317.16, default_y=-360.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=433.89, default_y=-365.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=506.84, default_y=-370.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=579.8, default_y=-365.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=696.16, default_y=-375.65):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-45.65, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=959.16, default_y=-340.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-45.65, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.39)
            with Note(default_x=83.7, default_y=-340.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.7, default_y=-355.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=159.7, default_y=-350.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=220.5, default_y=-355.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=296.51, default_y=-360.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=334.51, default_y=-365.64):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=372.15, default_y=-360.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.63, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=456.11, default_y=-375.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-50.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=516.92, default_y=-365.64):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
        with Measure(number='56', width=482.97):
            with Note(default_x=27.82, default_y=-375.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=77.56, default_y=-370.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=126.93, default_y=-375.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-50.63, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=245.42, default_y=-370.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=276.51, default_y=-365.64):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=307.23, default_y=-360.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=372.67, default_y=-360.64):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-50.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-345.82):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-350.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-350.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-350.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-345.82):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-365.82):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-350.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-350.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-335.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-345.82):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=25.46, default_y=-330.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=86.79, default_y=-335.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.88, default_y=-340.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.4, default_y=-330.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-345.82):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-368.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-373.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-353.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-363.35):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-368.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-358.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-353.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-348.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=142.02, default_y=-353.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-358.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-50.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=86.48, default_y=-353.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-358.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=3.73, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-437.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-442.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-437.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-440.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.38, default_y=-454.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-454.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-469.48):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.29, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-434.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-444.48):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-449.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-454.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-449.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-429.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-429.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-449.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=4.99, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-451.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-431.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=14.89, default_y=-446.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=1.69, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-466.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.17, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.85)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=334.1, default_y=-459.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=587.83, default_y=-439.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=822.17, default_y=-449.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
            with Note(default_x=949.03, default_y=-454.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-46.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.05)
            with Note(default_x=80.38, default_y=-464.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.59, default_y=-449.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
            with Note(default_x=214.79, default_y=-444.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=282.0, default_y=-444.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
            with Note(default_x=348.85, default_y=-449.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=10.69, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=540.37, default_y=-464.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='20', width=468.32):
            with Note(default_x=19.62, default_y=-459.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=73.81, default_y=-454.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=128.01, default_y=-449.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=195.75, default_y=-454.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=249.94, default_y=-459.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=304.14, default_y=-459.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
            with Note(default_x=357.97, default_y=-464.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.83, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('gamb/')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-433.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-433.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-468.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-453.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-44.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-458.63):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.2)
            with Note(default_x=89.18, default_y=-477.15):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-477.15):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-462.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.44, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-447.15):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-457.15):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-437.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-447.15):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-462.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-442.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-442.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-462.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.2, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.16)
            with Note(default_x=80.38, default_y=-454.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-434.06):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=14.89, default_y=-449.06):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-469.06):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-45.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note(default_x=223.82, default_y=-434.06):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-431.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=342.26, default_y=-441.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.09, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=551.77, default_y=-431.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=813.65, default_y=-436.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.09, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.38, default_y=-438.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=205.73, default_y=-453.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=393.75, default_y=-438.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=519.46, default_y=-443.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.73, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='38', width=493.75):
            with Note(default_x=27.86, default_y=-438.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=137.37, default_y=-453.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=379.32, default_y=-453.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.3)
            with Note(default_x=80.38, default_y=-453.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=342.26, default_y=-453.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.37, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
            with Note(default_x=552.13, default_y=-438.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=683.07, default_y=-438.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=813.65, default_y=-438.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-443.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.34, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-458.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-453.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-458.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-478.2):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.17)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=197.1, default_y=-458.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=323.45, default_y=-463.62):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=386.45, default_y=-468.62):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=449.45, default_y=-473.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=512.44, default_y=-478.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=575.44, default_y=-483.62):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-488.62):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.29, default_y=-493.62):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=123.41, default_y=-473.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=198.32, default_y=-493.62):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=326.9, default_y=-458.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-463.62):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.45)
            with Note(default_x=83.7, default_y=-457.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=267.96, default_y=-462.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.83, default_y=-467.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=452.23, default_y=-472.9):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=565.62, default_y=-477.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=679.02, default_y=-472.9):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=749.89, default_y=-467.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=820.4, default_y=-462.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.95)
            with Note(default_x=80.38, default_y=-499.55):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=310.72, default_y=-464.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.9, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
        with Measure(number='53', width=502.73):
            with Note(default_x=24.5, default_y=-464.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=266.43, default_y=-479.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=3.26, default_y=-45.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.85)
            with Note(default_x=80.38, default_y=-461.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=576.48, default_y=-456.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.18)
            with Note(default_x=80.38, default_y=-464.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=372.15, default_y=-469.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=456.11, default_y=-474.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=516.92, default_y=-479.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='56', width=482.97):
            with Note(default_x=22.92, default_y=-484.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=372.67, default_y=-469.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-40.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-465.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.82)
            with Note(default_x=80.38, default_y=-451.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-471.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-436.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-446.63):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-456.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-451.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-461.63):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=106.92, default_y=-471.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-466.63):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.82)
            with Note(default_x=80.38, default_y=-468.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-473.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-478.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-473.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-468.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-483.17):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-463.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=68.95, default_y=-463.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-448.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=86.48, default_y=-463.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-483.17):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=3.73, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-567.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-547.74):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-557.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-560.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.4)
            with Note(default_x=80.38, default_y=-540.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-540.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-545.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.08, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-545.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-540.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-535.88):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-530.88):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-535.88):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-540.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-540.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-545.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-546.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-551.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=16.47, default_y=-556.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=163.53, default_y=-561.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=216.0, default_y=-556.5):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-551.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.17, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-553.63):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-543.63):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-553.63):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-563.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-543.63):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=89.18, default_y=-552.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-552.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-557.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-557.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-552.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-547.15):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-542.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-547.15):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-552.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-552.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-557.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.99, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-549.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-554.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=16.47, default_y=-559.06):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=140.65, default_y=-564.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=184.32, default_y=-559.06):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-554.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='38', width=493.75):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.42)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=32.88, default_y=-553.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=74.23, default_y=-558.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.84, default_y=-563.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.14, default_y=-568.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=178.49, default_y=-563.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=32.06, default_y=-568.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=71.17, default_y=-553.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=107.33, default_y=-568.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=169.91, default_y=-563.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.83)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='50', width=437.46):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=198.32, default_y=-558.45):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-573.45):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.3)
            with Note(default_x=83.34, default_y=-555.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=452.23, default_y=-560.2):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=565.62, default_y=-565.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-570.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-575.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-584.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='53', width=502.73):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='56', width=482.97):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.05)
            with Note(default_x=80.38, default_y=-556.68):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-566.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-556.68):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-566.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-551.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-556.68):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-566.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-566.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-571.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-571.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=25.46, default_y=-566.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('reIch')
            with Note(default_x=62.98, default_y=-561.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=106.92, default_y=-556.68):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=184.92, default_y=-561.68):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
            with Note(default_x=222.44, default_y=-551.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.92, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.8)
            with Note(default_x=80.38, default_y=-544.97):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-559.97):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-554.97):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-559.97):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-564.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-569.97):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-574.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-579.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=142.02, default_y=-559.97):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-46.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='66', width=221.84):
            with Note(default_x=14.89, default_y=-559.97):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=11.48, default_y=-46.7, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-559.97):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=13.52, default_y=-46.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-653.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-633.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-638.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.3)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=81.95, default_y=-644.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=412.16, default_y=-654.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=742.37, default_y=-649.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.0)
            with Note(default_x=84.91, default_y=-646.88):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=138.07, default_y=-641.88):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=188.26, default_y=-636.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=273.31, default_y=-636.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-636.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=15.08, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-636.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-636.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-631.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-646.88):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-631.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-631.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-631.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-631.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=84.91, default_y=-641.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=141.25, default_y=-636.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=194.62, default_y=-631.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=284.76, default_y=-631.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=16.47, default_y=-636.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=163.53, default_y=-641.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=216.0, default_y=-636.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=33.88, default_y=-631.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.39, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-648.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-648.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-633.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=16.47, default_y=-643.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=80.74, default_y=-638.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=109.21, default_y=-633.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.0)
            with Note(default_x=89.18, default_y=-663.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-648.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=30.55, default_y=-648.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.65, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=96.46, default_y=-658.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=162.37, default_y=-653.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-653.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-658.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-643.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-648.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-648.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-648.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-658.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.99, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.82)
            with Note(default_x=81.95, default_y=-645.87):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=217.7, default_y=-640.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=265.82, default_y=-635.87):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=16.47, default_y=-640.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=140.65, default_y=-645.87):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=184.32, default_y=-640.87):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-635.87):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='38', width=493.75):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-648.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-643.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-648.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-643.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.08)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='50', width=437.46):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=198.32, default_y=-664.53):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-669.53):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.43)
            with Note(default_x=83.7, default_y=-654.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=267.96, default_y=-659.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.47, default_y=-664.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=679.02, default_y=-669.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=820.4, default_y=-659.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-679.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.34, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='53', width=502.73):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='56', width=482.97):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-630.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-645.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.95)
            with Note(default_x=80.38, default_y=-658.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-668.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-668.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-653.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-663.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-658.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-653.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-653.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-663.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-658.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-658.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('rech')
            with Note(default_x=106.92, default_y=-653.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-663.63):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-635.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.92, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.7)
            with Note(default_x=80.38, default_y=-672.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-652.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=227.27, default_y=-672.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=263.08, default_y=-657.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-677.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-662.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-662.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-667.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-672.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=142.02, default_y=-667.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='66', width=221.84):
            with Note(default_x=19.43, default_y=-662.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=10.38, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=55.22, default_y=-662.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=91.02, default_y=-667.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=126.81, default_y=-672.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=159.65, default_y=-667.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-662.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=13.52, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-768.74):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-758.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-758.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.95, default_y=-759.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=410.59, default_y=-774.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.95, default_y=-776.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=186.69, default_y=-761.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-43.35, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-766.88):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.29, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-766.88):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-766.88):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-756.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-776.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-43.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-756.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-761.88):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-761.88):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-756.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.78, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.3)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=81.95, default_y=-785.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=194.62, default_y=-770.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=284.76, default_y=-765.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=16.47, default_y=-765.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
            with Note(default_x=105.15, default_y=-780.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=216.0, default_y=-765.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=33.88, default_y=-765.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.39, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-763.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-763.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-753.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-758.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-753.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.3)
            with Note(default_x=89.18, default_y=-792.45):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                Accidental('natural')
                with Lyric(number='1', default_x=11.48, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-792.45):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=30.55, default_y=-787.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.65, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=96.46, default_y=-802.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=162.37, default_y=-797.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-797.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-787.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-787.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-787.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-782.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-42.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-802.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-42.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-802.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.2, default_y=-42.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-770.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.3)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=81.95, default_y=-790.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=163.67, default_y=-775.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=265.82, default_y=-770.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='down', line_type='solid', end_length=15.0, default_y=23.15)
            with Note(default_x=16.47, default_y=-770.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
            with Note(default_x=91.07, default_y=-785.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='down', end_length=15.0)
            with Note(default_x=184.32, default_y=-770.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-770.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='38', width=493.75):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-778.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-758.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=29.1, default_y=-778.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=105.75, default_y=-763.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=14.63, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='50', width=437.46):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=198.32, default_y=-794.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-809.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.7, default_y=-784.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=197.09, default_y=-794.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.47, default_y=-794.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-52.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=565.62, default_y=-779.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=679.02, default_y=-794.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=820.76, default_y=-774.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=891.63, default_y=-789.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=962.5, default_y=-789.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.71, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-804.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='53', width=502.73):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='56', width=482.97):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-760.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.38, default_y=-790.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-795.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-785.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-775.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-780.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Lyric(number='1', default_x=9.9, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-775.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-775.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-770.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-790.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-790.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-50.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-810.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=147.4, default_y=-810.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-50.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-790.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-50.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-765.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-787.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-802.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-787.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-792.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-777.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-782.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-782.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=109.23, default_y=-792.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note(default_x=142.02, default_y=-797.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-802.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=86.48, default_y=-797.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
        with Measure(number='67', width=162.63):
            with Note(default_x=19.43, default_y=-802.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Note(default_x=64.65, default_y=-797.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=82.75, default_y=-792.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=400.76):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=291.8):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=181.87):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-858.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie')
            with Note(default_x=112.58, default_y=-863.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=196.81, default_y=-858.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('leuch')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-874.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=11.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tet')
            with Note(default_x=742.37, default_y=-889.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.9)
            with Note(default_x=80.38, default_y=-878.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=273.31, default_y=-878.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-893.78):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.29, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('stern/')
            with Note(default_x=108.32, default_y=-858.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('voll')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-868.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gnad')
            with Note(default_x=112.92, default_y=-873.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.27, default_y=-878.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('War')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-873.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('heit')
            with Note(default_x=77.22, default_y=-853.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=137.94, default_y=-853.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-873.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=4.99, default_y=-45.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herrn/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-850.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=411.11, default_y=-870.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('süs')
            with Note(default_x=741.84, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-885.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wur')
            with Note(default_x=284.76, default_y=-865.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('zel')
        with Measure(number='16', width=309.6):
            with Note(default_x=14.89, default_y=-880.8):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jes')
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=33.88, default_y=-900.8):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.75, default_y=-45.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('se/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='20', width=468.32):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='23', width=234.77):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='24', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=49.76, default_y=-853.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=106.67, default_y=-853.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=163.58, default_y=-888.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Da')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-873.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-44.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('vid')
            with Note(default_x=109.21, default_y=-878.63):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-44.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.2)
            with Note(default_x=89.18, default_y=-920.65):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ja')
            with Note(default_x=185.6, default_y=-920.65):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('cobs')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-905.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.44, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stamm/')
            with Note(default_x=162.37, default_y=-890.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-900.65):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kö')
            with Note(default_x=101.08, default_y=-880.65):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('nig')
            with Note(default_x=141.59, default_y=-890.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-905.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
            with Note(default_x=93.39, default_y=-885.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Breu')
            with Note(default_x=164.89, default_y=-885.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ti')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-905.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.2, default_y=-40.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('gam/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-850.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hast')
            with Note(default_x=411.11, default_y=-870.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir')
            with Note(default_x=741.84, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-890.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz')
            with Note(default_x=265.82, default_y=-870.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='34', width=263.84):
            with Note(default_x=14.89, default_y=-885.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=1.69, default_y=-45.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ses')
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-905.17):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.77, default_y=-45.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='38', width=493.75):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='41', width=220.26):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-878.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=178.49, default_y=-873.62):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-878.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=169.91, default_y=-898.62):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='46', width=304.41):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='47', width=286.14):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='48', width=235.56):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='50', width=437.46):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=198.32, default_y=-894.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=381.38, default_y=-899.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.66)
            with Note(default_x=83.7, default_y=-900.29):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
            with Note(default_x=267.96, default_y=-905.29):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=338.83, default_y=-910.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=452.23, default_y=-915.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=565.62, default_y=-920.29):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-47.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=679.02, default_y=-915.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=749.89, default_y=-910.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=820.4, default_y=-905.29):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-919.55):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.7, default_y=-45.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='53', width=502.73):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='56', width=482.97):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-885.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lieb')
            with Note(default_x=698.62, default_y=-850.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.05, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.82)
            with Note(default_x=80.38, default_y=-896.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freund')
            with Note(default_x=178.05, default_y=-916.35):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-881.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('schön')
            with Note(default_x=79.06, default_y=-881.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=127.29, default_y=-876.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('herr')
            with Note(default_x=209.21, default_y=-896.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-881.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('gross')
            with Note(default_x=73.19, default_y=-891.35):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=118.17, default_y=-901.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ehr')
            with Note(default_x=194.87, default_y=-896.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=6.41, default_y=-47.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich/')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-906.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('reich')
            with Note(default_x=106.92, default_y=-916.35):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
            with Note(default_x=181.96, default_y=-911.35):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-47.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-865.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-902.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=152.0, default_y=-907.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=224.31, default_y=-912.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sehr')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-907.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('prech')
            with Note(default_x=95.45, default_y=-902.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tig')
            with Note(default_x=127.34, default_y=-917.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-897.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-45.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
            with Note(default_x=68.95, default_y=-897.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=5.13, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben/')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-882.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=86.48, default_y=-897.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-45.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ha')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-917.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
                with Lyric(number='1', default_x=3.73, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=507.13):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=102.68, default_y=-953.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=294.89, default_y=-953.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=400.03, default_y=-953.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=400.76):
            with Note(default_x=22.22, default_y=-963.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=95.36, default_y=-958.55):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.49, default_y=-953.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=179.75, default_y=-968.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=235.65, default_y=-948.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=336.92, default_y=-983.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
        with Measure(number='3', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.95, default_y=-960.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=329.96, default_y=-940.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=454.28, default_y=-950.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=578.6, default_y=-955.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=702.93, default_y=-960.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=827.25, default_y=-965.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=951.57, default_y=-960.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=317.86):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-983.74):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=178.97, default_y=-983.74):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=236.26, default_y=-968.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='5', width=291.8):
            with Note(default_x=16.46, default_y=-953.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=83.09, default_y=-973.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.23, default_y=-968.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.65, default_y=-963.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=190.79, default_y=-958.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=223.93, default_y=-953.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=257.06, default_y=-988.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=181.87):
            with Note(default_x=13.32, default_y=-968.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=114.88, default_y=-988.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=285.96):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-988.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=112.58, default_y=-993.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=196.81, default_y=-988.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='8', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-979.3):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=742.37, default_y=-994.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='9', width=363.27):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.95)
            with Note(default_x=80.38, default_y=-987.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=273.31, default_y=-987.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='10', width=166.26):
            with Note(default_x=21.92, default_y=-1002.73):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=108.32, default_y=-967.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='11', width=230.1):
            with Note(default_x=23.5, default_y=-977.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
            with Note(default_x=112.92, default_y=-982.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=154.27, default_y=-987.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=203.58):
            with Note(default_x=16.5, default_y=-982.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=77.22, default_y=-962.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=137.94, default_y=-962.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
        with Measure(number='13', width=114.28):
            with Note(default_x=24.22, default_y=-982.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-955.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=411.11, default_y=-975.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=741.84, default_y=-980.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='15', width=379.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-990.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=284.76, default_y=-970.8):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='16', width=309.6):
            with Note(default_x=14.89, default_y=-985.8):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
        with Measure(number='17', width=388.08):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=33.88, default_y=-1005.8):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=199.33, default_y=-1005.8):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-964.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=334.1, default_y=-984.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=587.83, default_y=-964.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=822.17, default_y=-974.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=949.03, default_y=-979.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=609.18):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-991.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.59, default_y=-976.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=214.79, default_y=-971.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=282.0, default_y=-971.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=348.85, default_y=-976.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
            with Note(default_x=540.37, default_y=-991.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=468.32):
            with Note(default_x=19.62, default_y=-986.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.81, default_y=-981.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=128.01, default_y=-976.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=195.75, default_y=-981.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=249.94, default_y=-986.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=304.14, default_y=-986.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=357.97, default_y=-991.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=198.32, default_y=-962.52):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=315.33, default_y=-957.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=432.34, default_y=-952.52):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=578.6, default_y=-947.52):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=724.87, default_y=-952.52):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=841.88, default_y=-957.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('5')
            with Note(default_x=958.88, default_y=-957.52):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='22', width=341.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-963.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=137.23, default_y=-983.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=208.29, default_y=-968.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=265.13, default_y=-973.63):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='23', width=234.77):
            with Note(default_x=24.06, default_y=-978.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=86.16, default_y=-983.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=128.32, default_y=-963.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=111.9):
            with Note(default_x=13.32, default_y=-963.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.15, default_y=-983.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='25', width=225.41):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
                with Clef(after_barline='yes'):
                    Sign('F')
                    Line(4)
            with Note(default_x=49.76, default_y=-958.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=106.67, default_y=-958.63):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=163.58, default_y=-993.63):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='26', width=164.41):
            with Note(default_x=14.89, default_y=-978.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=109.21, default_y=-983.63):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='27', width=249.81):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.87)
            with Note(default_x=89.18, default_y=-1026.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
                with Lyric(number='1', default_x=1.69, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=185.6, default_y=-1026.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
        with Measure(number='28', width=233.2):
            with Note(default_x=28.98, default_y=-1011.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=162.37, default_y=-996.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=216.06):
            with Note(default_x=13.32, default_y=-1006.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
            with Note(default_x=101.08, default_y=-986.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=141.59, default_y=-996.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='30', width=241.31):
            with Note(default_x=21.9, default_y=-1011.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=93.39, default_y=-991.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=164.89, default_y=-991.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
        with Measure(number='31', width=137.12):
            with Note(default_x=17.01, default_y=-1011.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-955.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=411.11, default_y=-975.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=741.84, default_y=-980.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='33', width=352.46):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-995.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=265.82, default_y=-975.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='34', width=263.84):
            with Note(default_x=14.89, default_y=-990.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
        with Measure(number='35', width=461.19):
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
            with Note(default_x=32.31, default_y=-1010.17):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=223.82, default_y=-975.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='36', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-956.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=342.26, default_y=-966.9):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=551.77, default_y=-956.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=813.65, default_y=-961.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='37', width=583.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-963.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=205.73, default_y=-978.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
            with Note(default_x=394.11, default_y=-963.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('3')
            with Note(default_x=456.79, default_y=-963.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2')
            with Note(default_x=519.46, default_y=-968.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='38', width=493.75):
            with Note(default_x=27.86, default_y=-963.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=140.33, default_y=-978.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=266.85, default_y=-978.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
                with Lyric(number='2', default_x=6.22, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=379.32, default_y=-978.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='39', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-978.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
                with Lyric(number='2', default_x=6.22, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=342.26, default_y=-978.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=552.13, default_y=-963.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=683.07, default_y=-963.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=813.65, default_y=-963.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='40', width=380.05):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-968.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=240.34, default_y=-953.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=316.87, default_y=-948.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='41', width=220.26):
            with Note(default_x=19.18, default_y=-943.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=53.57, default_y=-933.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.6, default_y=-948.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=139.67, default_y=-933.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='42', width=239.77):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=28.35, default_y=-983.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=178.49, default_y=-978.62):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='43', width=237.42):
            with Note(default_x=27.52, default_y=-983.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=169.91, default_y=-1003.62):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='44', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-960.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=691.57, default_y=-955.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='45', width=251.39):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-966.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=183.19, default_y=-986.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='46', width=304.41):
            with Note(default_x=27.86, default_y=-961.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=80.66, default_y=-951.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=130.51, default_y=-966.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=215.0, default_y=-966.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='47', width=286.14):
            with Note(default_x=25.26, default_y=-986.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=75.05, default_y=-986.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=121.88, default_y=-981.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=201.55, default_y=-966.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='48', width=235.56):
            with Note(default_x=21.9, default_y=-961.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=84.04, default_y=-951.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=146.19, default_y=-966.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='49', width=640.04):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
                with Clef(after_barline='yes'):
                    Sign('F')
                    Line(4)
            with Note(default_x=134.1, default_y=-999.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=323.45, default_y=-1004.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=386.45, default_y=-1009.53):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=449.45, default_y=-1014.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=512.44, default_y=-1019.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=575.44, default_y=-1024.53):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='50', width=437.46):
            with Note(default_x=14.82, default_y=-1029.53):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.29, default_y=-1034.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=123.41, default_y=-1014.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=198.32, default_y=-1034.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=326.9, default_y=-999.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=381.38, default_y=-1004.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='51', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.05)
            with Note(default_x=83.7, default_y=-1015.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=267.96, default_y=-1020.34):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=338.83, default_y=-1025.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=452.23, default_y=-1030.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=565.62, default_y=-1035.34):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=679.02, default_y=-1030.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=749.89, default_y=-1025.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=820.4, default_y=-1020.34):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='52', width=574.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-1024.55):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=313.68, default_y=-989.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=443.24, default_y=-989.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
        with Measure(number='53', width=502.73):
            with Note(default_x=27.46, default_y=-989.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=148.42, default_y=-989.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=269.39, default_y=-1004.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=393.24, default_y=-1004.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.22, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
        with Measure(number='54', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.34, default_y=-986.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.22, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.22, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=316.8, default_y=-986.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=579.44, default_y=-981.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=842.08, default_y=-981.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.94, default_y=-47.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-73.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
        with Measure(number='55', width=594.52):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=83.34, default_y=-989.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-47.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.94, default_y=-73.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=220.14, default_y=-989.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=372.15, default_y=-994.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=456.11, default_y=-999.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=516.92, default_y=-1004.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
        with Measure(number='56', width=482.97):
            with Note(default_x=27.46, default_y=-1009.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.22, default_y=-73.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=126.93, default_y=-1009.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=195.32, default_y=-1009.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=6.22, default_y=-47.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('56')
                with Lyric(number='2', default_x=6.22, default_y=-73.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('34')
            with Note(default_x=307.23, default_y=-1009.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=372.67, default_y=-994.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='57', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('1')
            with Note(default_x=98.72, default_y=-990.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=698.62, default_y=-955.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='58', width=243.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.3)
            with Note(default_x=80.38, default_y=-1003.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note(default_x=178.05, default_y=-1023.65):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='59', width=296.05):
            with Note(default_x=27.86, default_y=-988.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=79.06, default_y=-988.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=127.29, default_y=-983.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
            with Note(default_x=209.21, default_y=-1003.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='60', width=276.49):
            with Note(default_x=25.26, default_y=-988.65):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=73.19, default_y=-998.65):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=118.17, default_y=-1008.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=194.87, default_y=-1003.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='61', width=261.92):
            with Note(default_x=22.5, default_y=-1013.65):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=106.92, default_y=-1023.65):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=181.96, default_y=-1018.65):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('#')
        with Measure(number='62', width=1077.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-970.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='63', width=300.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.0)
            with Note(default_x=80.38, default_y=-1012.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=152.0, default_y=-1017.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=3.26, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('6')
            with Note(default_x=224.31, default_y=-1022.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='64', width=188.03):
            with Note(default_x=24.5, default_y=-1017.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
            with Note(default_x=95.45, default_y=-1012.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=127.34, default_y=-1027.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='65', width=204.15):
            with Note(default_x=13.32, default_y=-1007.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=68.95, default_y=-1007.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
        with Measure(number='66', width=221.84):
            with Note(default_x=16.47, default_y=-992.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=86.48, default_y=-1007.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('breve')
        with Measure(number='67', width=162.63):
            with Note(default_x=14.89, default_y=-1027.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('breve')
                Dot()
            with Barline(location='right'):
                BarStyle('light-heavy')