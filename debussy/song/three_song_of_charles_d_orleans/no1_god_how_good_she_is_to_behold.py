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
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P2-I1', port=2)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P3-I1', port=3)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P4-I1', port=4)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=331.88):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(93.8)
                        RightMargin(0.0)
                    TopSystemDistance(268.89)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(5)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.94, default_y=32.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Très modéré soutenu et expressif', default_y=11.29, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='9.8')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.94, default_y=63.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.94, default_y=94.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.94, default_y=125.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=214.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=8.99, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=449.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=22.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=70.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=161.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=209.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=300.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=349.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
        with Measure(number='3', width=202.52):
            with Note(default_x=16.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=130.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
        with Measure(number='4', width=493.03):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=121.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=159.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=237.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=275.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=358.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=425.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=206.3):
            with Note(default_x=16.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Note(default_x=81.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.06, default_y=-80.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('le;')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=371.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pour')
            with Note(default_x=64.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('les')
                    Extend()
            with Note(default_x=89.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=117.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('gran')
            with Note(default_x=161.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('biens')
            with Note(default_x=256.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=304.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sont')
            with Note(default_x=337.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
        with Measure(number='7', width=440.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=130.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('el')
            with Note(default_x=165.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                    Extend()
            with Note(default_x=259.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='8', width=331.5):
            with Note(default_x=17.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chas')
            with Note(default_x=60.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cun')
            with Note(default_x=95.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('est')
            with Note(default_x=131.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('prest')
            with Note(default_x=173.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=216.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=251.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=295.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=299.28):
            with Note(default_x=17.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('loü')
            with Note(default_x=53.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=84.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('er.')
                    Extend()
            with Note(default_x=128.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=213.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    with Articulations():
                        BreathMark(None)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=262.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
        with Measure(number='10', width=414.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=125.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=168.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pour')
            with Note(default_x=211.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('roit')
            with Note(default_x=254.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text("d'el")
            with Note(default_x=310.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=353.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('las')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='11', width=188.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=15.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=10.91, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser?')
            with Note(default_x=98.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tous')
            with Note(default_x=125.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=159.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='12', width=468.52):
            with Note(default_x=25.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('jours')
            with Note(default_x=94.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sa')
                    Extend()
            with Note(default_x=120.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('beau')
            with Note(default_x=244.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('té')
                    Extend()
            with Note(default_x=270.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=321.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=390.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nou')
            with Note(default_x=415.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=441.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=322.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=121.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vel')
            with Note(default_x=182.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=259.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu')
        with Measure(number='14', width=445.34):
            with Note(default_x=22.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=70.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=118.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=197.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=271.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=345.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=375.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=413.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='15', width=303.57):
            with Note(default_x=17.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.82, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
            with Note(default_x=122.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=217.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=259.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
        with Measure(number='16', width=426.43):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=132.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=182.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=232.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=297.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='17', width=166.48):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=16.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=73.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.9, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('le!')
        with Measure(number='18', width=302.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.03, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Par')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.03)
            with Note(default_x=78.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=108.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.92, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ça,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=155.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.03)
            with Note(default_x=184.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=214.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.76, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('là,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=271.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=175.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('mer')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Note(default_x=113.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ne')
        with Measure(number='20', width=375.56):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=133.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('scay')
            with Note(default_x=191.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=232.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=273.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Note(default_x=303.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=336.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('moi')
        with Measure(number='21', width=285.16):
            with Note(default_x=14.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sel')
            with Note(default_x=100.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=138.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
            with Note(default_x=188.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('soit')
            with Note(default_x=236.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
        with Measure(number='22', width=410.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('tous')
                    Extend()
            with Note(default_x=75.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=140.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bien')
                    Extend()
            with Note(default_x=202.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=228.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=285.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=347.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('fais')
        with Measure(number='23', width=435.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=130.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tel')
            with Note(default_x=223.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                with Lyric(number='1', default_x=8.46, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note(default_x=316.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("C'est")
            with Note(default_x=375.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ung')
        with Measure(number='24', width=344.11):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('son')
            with Note(default_x=94.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=152.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=211.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'i")
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=269.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pen')
            with Note(default_x=306.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='25', width=291.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.51, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser:')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Plus lent', relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='9.8')
            with Note(default_x=198.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.35, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='26', width=466.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.2)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=121.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=160.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=233.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=272.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=345.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=384.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
        with Measure(number='27', width=173.5):
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.42, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Note(default_x=68.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=9.71, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='28', width=324.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=22.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=56.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=77.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=185.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=237.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=271.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
        with Measure(number='29', width=106.41):
            with Note(default_x=16.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.78, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=331.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(105.69)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(5)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=214.8, default_y=-195.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=8.99, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=449.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=22.02, default_y=-185.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=70.38, default_y=-190.69):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=100.71, default_y=-185.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.05, default_y=-190.69):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=161.38, default_y=-195.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=209.74, default_y=-180.69):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=300.74, default_y=-185.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=349.11, default_y=-190.69):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=379.44, default_y=-185.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=417.36, default_y=-190.69):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='3', width=202.52):
            with Note(default_x=16.86, default_y=-195.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=130.27, default_y=-195.69):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
        with Measure(number='4', width=493.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(119.1)
            with Note(default_x=121.21, default_y=-199.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=159.07, default_y=-199.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_y=-81.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=198.48, default_y=-194.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=237.89, default_y=-189.1):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=275.75, default_y=-194.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-81.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
                    Extend()
            with Note(default_x=299.49, default_y=-189.1):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.24, default_y=-194.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=358.92, default_y=-199.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=425.58, default_y=-204.1):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=206.3):
            with Note(default_x=16.62, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Note(default_x=81.59, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.06, default_y=-81.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('le;')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=371.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.57, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.42, default_y=-204.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pour')
            with Note(default_x=64.96, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('les')
                    Extend()
            with Note(default_x=89.32, default_y=-204.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=117.61, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('gran')
            with Note(default_x=161.91, default_y=-204.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('biens')
            with Note(default_x=256.98, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=304.52, default_y=-204.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('sont')
            with Note(default_x=337.44, default_y=-209.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-81.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
        with Measure(number='7', width=440.51):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(116.4)
            with Note(default_x=130.01, default_y=-211.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('el')
            with Note(default_x=165.32, default_y=-206.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=196.82, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                    Extend()
            with Note(default_x=259.92, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='8', width=331.5):
            with Note(default_x=17.62, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chas')
            with Note(default_x=60.72, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cun')
            with Note(default_x=95.53, default_y=-196.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('est')
            with Note(default_x=131.23, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('prest')
            with Note(default_x=173.67, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=216.77, default_y=-206.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=251.58, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=295.09, default_y=-206.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=299.28):
            with Note(default_x=17.82, default_y=-211.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('loü')
            with Note(default_x=53.12, default_y=-206.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=84.63, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=0.4, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('er.')
                    Extend()
            with Note(default_x=128.24, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=213.31, default_y=-201.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    with Articulations():
                        BreathMark(None)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=262.79, default_y=-206.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
        with Measure(number='10', width=414.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(129.2)
            with Note(default_x=125.01, default_y=-224.2):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=168.15, default_y=-219.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pour')
            with Note(default_x=211.28, default_y=-209.2):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('roit')
            with Note(default_x=254.41, default_y=-209.2):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text("d'el")
            with Note(default_x=310.47, default_y=-204.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=353.61, default_y=-204.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('las')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='11', width=188.62):
            with Note(default_x=15.73, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=0.4, default_y=-80.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser?')
                    Extend()
            with Note(default_x=65.17, default_y=-204.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=98.42, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
        with Measure(number='12', width=468.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=25.62, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tous')
            with Note(default_x=60.09, default_y=-194.2):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=94.57, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('jours')
            with Note(default_x=175.29, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('sa')
            with Note(default_x=209.76, default_y=-194.2):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('beau')
            with Note(default_x=244.86, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('té')
            with Note(default_x=321.42, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=355.89, default_y=-189.2):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nou')
            with Note(default_x=390.37, default_y=-199.2):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-80.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vel')
        with Measure(number='13', width=322.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(128.82)
            with Note(default_x=121.21, default_y=-198.82):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.62, default_y=-208.82):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=445.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
            with Note(default_x=155.44, default_y=-183.82):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu')
            with Note(default_x=197.74, default_y=-188.82):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=234.65, default_y=-193.82):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=271.55, default_y=-198.82):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=308.46, default_y=-198.82):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=345.37, default_y=-193.82):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=394.55, default_y=-188.82):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
        with Measure(number='15', width=303.57):
            with Note(default_x=17.22, default_y=-188.82):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
                    Extend()
            with Note(default_x=43.58, default_y=-193.82):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.95, default_y=-198.82):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.32, default_y=-203.82):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=122.68, default_y=-198.82):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=191.23, default_y=-203.82):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=217.6, default_y=-208.82):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=259.78, default_y=-213.82):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
        with Measure(number='16', width=426.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(146.35)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=132.42, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=182.25, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=232.09, default_y=-236.35):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=297.25, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=347.08, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=373.75, default_y=-226.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.29, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='17', width=166.48):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=16.62, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=73.28, default_y=-236.35):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.9, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('le!')
        with Measure(number='18', width=302.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.17, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.4, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.03, default_y=-241.35):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Par')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-91.17)
            with Note(default_x=78.56, default_y=-246.35):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=108.05, default_y=-241.35):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.92, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ça,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=155.23, default_y=-246.35):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-91.17)
            with Note(default_x=184.72, default_y=-246.35):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=214.21, default_y=-241.35):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.76, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('là,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.85)
            with Note(default_x=271.75, default_y=-241.35):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=175.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.85, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.59, default_y=-231.35):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('mer')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Note(default_x=113.95, default_y=-241.35):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ne')
        with Measure(number='20', width=375.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(130.31)
            with Note(default_x=133.25, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('scay')
            with Note(default_x=191.93, default_y=-215.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=232.57, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=273.2, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Note(default_x=303.28, default_y=-215.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=336.58, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('moi')
        with Measure(number='21', width=285.16):
            with Note(default_x=14.82, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sel')
            with Note(default_x=100.26, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=138.23, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
                    Extend()
            with Note(default_x=164.89, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.63, default_y=-215.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('soit')
                    Extend()
            with Note(default_x=212.36, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.09, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
            with Note(default_x=259.82, default_y=-200.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=410.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=14.0, default_y=-195.31):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('tous')
                    Extend()
            with Note(default_x=44.95, default_y=-200.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.91, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.81, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.76, default_y=-215.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bien')
                    Extend()
            with Note(default_x=171.71, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.66, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.91, default_y=-200.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.16, default_y=-195.31):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=316.12, default_y=-200.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=347.07, default_y=-205.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('fais')
                    Extend()
            with Note(default_x=378.02, default_y=-210.31):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=435.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(120.72)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=130.01, default_y=-200.72):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tel')
            with Note(default_x=223.47, default_y=-205.72):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                with Lyric(number='1', default_x=8.46, default_y=-98.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note(default_x=316.92, default_y=-205.72):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('single')
                    Text("C'est")
            with Note(default_x=375.34, default_y=-200.72):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('ung')
        with Measure(number='24', width=344.11):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.43)
            with Note(default_x=14.0, default_y=-210.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('son')
            with Note(default_x=94.3, default_y=-215.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=152.71, default_y=-210.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=211.11, default_y=-200.72):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'i")
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-101.42)
            with Note(default_x=269.51, default_y=-205.72):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-98.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pen')
        with Measure(number='25', width=291.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.17, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-210.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-98.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser:')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=106.08, default_y=-215.72):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=198.16, default_y=-210.72):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.35, default_y=-98.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='26', width=466.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(129.0)
            with Note(default_x=121.21, default_y=-209.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=160.17, default_y=-214.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=184.6, default_y=-209.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.04, default_y=-214.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=233.47, default_y=-219.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=272.43, default_y=-204.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=345.73, default_y=-209.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=384.69, default_y=-214.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=409.12, default_y=-209.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.45, default_y=-214.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='27', width=173.5):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.18, default_y=-219.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.42, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=120.33, default_y=-194.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.35, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='28', width=324.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=22.02, default_y=-199.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=56.06, default_y=-204.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=93.08, default_y=-199.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.03, default_y=-194.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=185.1, default_y=-194.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=237.18, default_y=-199.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=271.22, default_y=-204.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=297.26, default_y=-209.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=106.41):
            with Note(default_x=16.82, default_y=-204.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=331.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(128.19)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(5)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=214.8, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=8.99, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=449.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=22.02, default_y=-328.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=70.38, default_y=-333.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=161.38, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=209.74, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
                    Extend()
            with Note(default_x=240.08, default_y=-333.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.41, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=300.74, default_y=-328.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=349.11, default_y=-333.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=379.44, default_y=-328.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=417.36, default_y=-333.87):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='3', width=202.52):
            with Note(default_x=16.86, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.22, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=130.27, default_y=-338.87):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
        with Measure(number='4', width=493.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(125.52)
            with Note(default_x=121.21, default_y=-344.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=159.07, default_y=-344.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-87.87, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=182.82, default_y=-339.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.15, default_y=-334.62):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.89, default_y=-329.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=275.75, default_y=-334.62):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-87.87, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=299.49, default_y=-329.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.24, default_y=-334.62):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=358.92, default_y=-339.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=462.48, default_y=-344.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=206.3):
            with Note(default_x=16.62, default_y=-344.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-87.87, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Note(default_x=45.49, default_y=-349.62):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=63.54, default_y=-354.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=81.59, default_y=-359.62):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.06, default_y=-87.87, relative_y=-30.0):
                    Syllabic('end')
                    Text('le;')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=371.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=209.45, default_y=-349.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pour')
            with Note(default_x=256.98, default_y=-339.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('les')
            with Note(default_x=304.52, default_y=-349.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-87.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('gran')
        with Measure(number='7', width=440.51):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(123.91)
            with Note(default_x=130.01, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('biens')
            with Note(default_x=196.82, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
                    Extend()
            with Note(default_x=260.29, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=291.59, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sont')
            with Note(default_x=322.89, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
            with Note(default_x=366.32, default_y=-355.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('el')
            with Note(default_x=402.62, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=331.5):
            with Note(default_x=17.62, default_y=-355.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.67, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chas')
            with Note(default_x=216.77, default_y=-335.31):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cun')
            with Note(default_x=273.33, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('est')
        with Measure(number='9', width=299.28):
            with Note(default_x=17.82, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('prest')
            with Note(default_x=84.63, default_y=-335.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=128.24, default_y=-330.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=163.13, default_y=-335.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('loü')
            with Note(default_x=213.31, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        BreathMark(None)
                with Lyric(number='1', default_x=8.71, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('er.')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=262.79, default_y=-345.31):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
        with Measure(number='10', width=414.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(119.79)
            with Note(default_x=125.01, default_y=-359.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=168.15, default_y=-354.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pour')
            with Note(default_x=211.28, default_y=-349.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('roit')
            with Note(default_x=281.37, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text("d'el")
            with Note(default_x=310.47, default_y=-344.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=380.57, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('las')
        with Measure(number='11', width=188.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=15.37, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=11.63, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser?')
            with Note(default_x=98.42, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tous')
            with Note(default_x=125.68, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=159.76, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='12', width=468.52):
            with Note(default_x=25.62, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('jours')
            with Note(default_x=94.57, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sa')
                    Extend()
            with Note(default_x=120.09, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.6, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.29, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('beau')
            with Note(default_x=244.86, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('té')
                    Extend()
            with Note(default_x=270.38, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.9, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=321.42, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=390.37, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nou')
            with Note(default_x=415.88, default_y=-334.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=441.4, default_y=-339.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=322.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(119.92)
            with Note(default_x=121.21, default_y=-333.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vel')
            with Note(default_x=182.62, default_y=-343.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=445.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=271.55, default_y=-343.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
        with Measure(number='15', width=303.57):
            with Note(default_x=17.22, default_y=-328.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=69.95, default_y=-333.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
                    Extend()
            with Note(default_x=96.32, default_y=-338.74):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.68, default_y=-333.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=191.23, default_y=-338.74):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=217.6, default_y=-343.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=259.78, default_y=-348.74):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
        with Measure(number='16', width=426.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(146.35)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=132.42, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=182.25, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=232.09, default_y=-397.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=297.25, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=347.08, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=373.75, default_y=-387.7):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.29, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='17', width=166.48):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=16.62, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=73.28, default_y=-397.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.9, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('le!')
        with Measure(number='18', width=302.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.03, default_y=-402.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Par')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=78.56, default_y=-407.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=108.05, default_y=-402.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.92, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ça,')
            with Note(default_x=155.23, default_y=-407.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=184.72, default_y=-407.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=214.21, default_y=-402.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.76, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('là,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=271.75, default_y=-402.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=175.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.59, default_y=-392.7):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.94, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('mer')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Note(default_x=113.95, default_y=-382.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ne')
        with Measure(number='20', width=375.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(126.65)
            with Note(default_x=133.25, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('scay')
            with Note(default_x=191.93, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=232.57, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=273.2, default_y=-361.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Note(default_x=303.28, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=336.58, default_y=-361.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('moi')
        with Measure(number='21', width=285.16):
            with Note(default_x=14.82, default_y=-361.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-55.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sel')
            with Note(default_x=52.79, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.52, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.26, default_y=-346.96):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=410.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=75.91, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
            with Note(default_x=109.81, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('soit')
            with Note(default_x=140.76, default_y=-361.96):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
            with Note(default_x=171.71, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('tous')
            with Note(default_x=202.66, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-55.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('bien')
                    Extend()
            with Note(default_x=243.91, default_y=-346.96):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.16, default_y=-341.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-55.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=316.12, default_y=-346.96):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=347.07, default_y=-351.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-55.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('fais')
                    Extend()
            with Note(default_x=378.02, default_y=-356.96):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=435.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(158.79)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=130.01, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tel')
            with Note(default_x=223.47, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note(default_x=316.92, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("C'est")
            with Note(default_x=375.34, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ung')
        with Measure(number='24', width=344.11):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=14.0, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('son')
            with Note(default_x=94.3, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=152.71, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=211.11, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'i")
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=269.51, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pen')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='25', width=291.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.64, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.51, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser:')
            with Note(default_x=198.16, default_y=-384.52):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.35, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='26', width=466.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(132.04)
            with Note(default_x=121.21, default_y=-356.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=160.17, default_y=-361.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=233.47, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=272.43, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
                    Extend()
            with Note(default_x=296.86, default_y=-361.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.3, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=345.73, default_y=-356.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=384.69, default_y=-361.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=409.12, default_y=-356.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.45, default_y=-361.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='27', width=173.5):
            with Direction(placement='above'):
                with DirectionType():
                    Words('più', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.18, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.42, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Note(default_x=68.39, default_y=-341.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=9.71, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='28', width=324.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=22.02, default_y=-356.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=56.06, default_y=-351.04):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
                    Extend()
            with Note(default_x=93.08, default_y=-346.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.03, default_y=-341.04):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=159.07, default_y=-346.04):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.1, default_y=-351.04):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=211.14, default_y=-356.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=237.18, default_y=-361.04):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=271.22, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=297.26, default_y=-371.04):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=106.41):
            with Note(default_x=16.82, default_y=-366.04):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=331.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(130.43)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(5)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=214.8, default_y=-494.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=9.71, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=449.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=22.02, default_y=-509.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=70.38, default_y=-509.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=161.38, default_y=-494.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=209.74, default_y=-494.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=300.74, default_y=-509.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=349.11, default_y=-504.31):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=398.4, default_y=-499.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=202.52):
            with Note(default_x=16.86, default_y=-494.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.94, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=130.27, default_y=-494.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
        with Measure(number='4', width=493.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(159.47)
            with Note(default_x=121.21, default_y=-539.09):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=159.07, default_y=-544.09):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=237.89, default_y=-549.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-77.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=358.92, default_y=-549.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=387.88, default_y=-549.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Note(default_x=425.58, default_y=-544.09):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=462.48, default_y=-539.09):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
        with Measure(number='5', width=206.3):
            with Note(default_x=16.62, default_y=-534.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-77.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Note(default_x=81.59, default_y=-534.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=110.47, default_y=-539.09):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.51, default_y=-544.09):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.56, default_y=-549.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=175.44, default_y=-534.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.06, default_y=-77.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('le;')
        with Measure(number='6', width=371.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=161.91, default_y=-534.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pour')
            with Note(default_x=256.98, default_y=-524.09):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('les')
            with Note(default_x=304.52, default_y=-534.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('gran')
        with Measure(number='7', width=440.51):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(127.85)
            with Note(default_x=130.01, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('biens')
            with Note(default_x=224.59, default_y=-483.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Note(default_x=260.29, default_y=-478.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('sont')
            with Note(default_x=338.56, default_y=-483.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
            with Note(default_x=366.32, default_y=-488.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('el')
            with Note(default_x=402.62, default_y=-478.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=331.5):
            with Note(default_x=17.62, default_y=-488.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.67, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chas')
            with Note(default_x=216.77, default_y=-488.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('cun')
            with Note(default_x=273.33, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('est')
        with Measure(number='9', width=299.28):
            with Note(default_x=17.82, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('prest')
            with Note(default_x=106.43, default_y=-488.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=128.24, default_y=-483.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=184.93, default_y=-488.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('loü')
            with Note(default_x=213.31, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        BreathMark(None)
                with Lyric(number='1', default_x=8.71, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('er.')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=262.79, default_y=-498.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
        with Measure(number='10', width=414.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(137.42)
            with Note(default_x=125.01, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=168.15, default_y=-516.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pour')
            with Note(default_x=211.28, default_y=-521.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('roit')
            with Note(default_x=254.41, default_y=-531.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text("d'el")
            with Note(default_x=310.47, default_y=-516.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=353.61, default_y=-526.41):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('las')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='11', width=188.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=15.37, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=11.63, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser?')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=142.72, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Tous')
        with Measure(number='12', width=468.52):
            with Note(default_x=25.62, default_y=-531.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('jours')
            with Note(default_x=94.57, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('sa')
            with Note(default_x=175.29, default_y=-496.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('beau')
            with Note(default_x=244.86, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('té')
            with Note(default_x=321.42, default_y=-531.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=390.37, default_y=-511.41):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-80.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nou')
        with Measure(number='13', width=322.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(139.7)
            with Note(default_x=121.21, default_y=-498.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vel')
            with Note(default_x=182.62, default_y=-498.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-77.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=445.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=303.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=122.68, default_y=-498.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-77.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('La')
                    Extend()
            with Note(default_x=164.87, default_y=-508.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=217.6, default_y=-513.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=259.78, default_y=-518.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-77.1, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
        with Measure(number='16', width=426.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(152.35)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=132.42, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('eu')
            with Note(default_x=182.25, default_y=-580.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=232.09, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('bonne')
            with Note(default_x=297.25, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('et')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=347.08, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=373.75, default_y=-565.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.29, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='17', width=166.48):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=16.62, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bel')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=73.28, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.62, default_y=-101.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('le!')
        with Measure(number='18', width=302.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.41, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.85, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.15, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.03, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Par')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-86.41)
            with Note(default_x=78.56, default_y=-605.05):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=108.05, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.92, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ça,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=155.23, default_y=-605.05):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-86.15)
            with Note(default_x=184.72, default_y=-605.05):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=214.21, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.76, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('là,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=271.75, default_y=-585.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=175.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.59, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.94, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('mer')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=20.0, font_style='italic', font_family='Arial', font_size='8.4')
            with Note(default_x=113.95, default_y=-575.05):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-101.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ne')
        with Measure(number='20', width=375.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(109.52)
            with Note(default_x=133.25, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('scay')
            with Note(default_x=191.93, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=232.57, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('me')
            with Note(default_x=273.2, default_y=-496.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne')
            with Note(default_x=303.28, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=336.58, default_y=-496.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('moi')
        with Measure(number='21', width=285.16):
            with Note(default_x=14.82, default_y=-506.48):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sel')
            with Note(default_x=100.26, default_y=-506.48):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=138.23, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Qui')
                    Extend()
            with Note(default_x=164.89, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.63, default_y=-496.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('soit')
                    Extend()
            with Note(default_x=212.36, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.09, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('en')
                    Extend()
            with Note(default_x=259.82, default_y=-481.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=410.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=14.0, default_y=-476.48):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('tous')
                    Extend()
            with Note(default_x=44.95, default_y=-481.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.91, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.81, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.76, default_y=-496.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('bien')
                    Extend()
            with Note(default_x=171.71, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.66, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.91, default_y=-481.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.16, default_y=-476.48):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=316.12, default_y=-481.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=347.07, default_y=-486.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-78.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('fais')
                    Extend()
            with Note(default_x=378.02, default_y=-491.48):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=435.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(128.06)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=130.01, default_y=-537.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tel')
            with Note(default_x=223.47, default_y=-537.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.46, default_y=-96.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('le.')
            with Note(default_x=316.92, default_y=-557.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('single')
                    Text("C'est")
            with Note(default_x=375.34, default_y=-552.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ung')
        with Measure(number='24', width=344.11):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=14.0, default_y=-542.58):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('son')
            with Note(default_x=94.3, default_y=-547.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=152.71, default_y=-542.58):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('que')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=211.11, default_y=-532.58):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'i")
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-99.25)
            with Note(default_x=269.51, default_y=-537.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-96.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pen')
        with Measure(number='25', width=291.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-542.58):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=0.4, default_y=-96.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser:')
                    Extend()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=106.08, default_y=-547.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=198.16, default_y=-537.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.35, default_y=-96.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu!')
        with Measure(number='26', width=466.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(121.43)
            with Note(default_x=121.21, default_y=-527.47):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text("qu'il")
            with Note(default_x=160.17, default_y=-527.47):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('la')
            with Note(default_x=233.47, default_y=-512.47):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('fait')
            with Note(default_x=272.43, default_y=-512.47):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=345.73, default_y=-527.47):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=384.69, default_y=-522.47):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-50.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
            with Note(default_x=424.79, default_y=-517.47):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=173.5):
            with Note(default_x=17.18, default_y=-512.47):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=9.42, default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='28', width=324.89):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=185.1, default_y=-522.47):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('bon')
            with Note(default_x=237.18, default_y=-517.47):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=271.22, default_y=-527.47):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gar')
        with Measure(number='29', width=106.41):
            with Note(default_x=16.82, default_y=-547.47):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.06, default_y=-50.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('der!')
            with Barline(location='right'):
                BarStyle('light-heavy')