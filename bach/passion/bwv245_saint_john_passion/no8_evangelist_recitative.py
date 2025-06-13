with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 245')
        WorkTitle('Saint John Passion')
    MovementNumber('BWV 245 NBA #8')
    MovementTitle('Simon Petrus aber folgete Jesu nach, und ein ander Jünger')
    with Identification():
        Creator('Edward J. Maurath', type='arranger')
        Creator('Johann Sebastian Bach (1685--1750)', type='composer')
        Creator('Saint John (Gospel)', type='lyricist')
        Creator('Baroque Passion Oratorio', type='poet')
        Creator('Martin Luthor', type='translator')
        Rights('Sequenced by Edward J. Maurath')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/272961/scores/5422847')
    with Defaults():
        with Scaling():
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2448.98)
            PageWidth(1581.64)
            with PageMargins(type='both'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Simon Petrus aber folgete Jesu nach, und ein ander Jünger', default_x=790.82, default_y=2392.29, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Recitative for the Evangelist, BWV 245, Saint John Passion, 1724, NBA #8 \n', default_x=790.82, default_y=2335.6, justify='center', valign='top', font_size='14')
        CreditWords('More at http://bach.ejmaurath.com')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)', default_x=1524.95, default_y=1558.51, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Martin Luther 1521 Translation of the Gospel of John', default_x=56.6894, default_y=1558.51, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=790.82, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Tenore')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Voice')
            with ScoreInstrument(id='P1-I2'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(0.0)
                Pan(0.0)
            MidiDevice(None, id='P1-I2', port=1)
            with MidiInstrument(id='P1-I2'):
                MidiChannel(2)
                MidiProgram(42)
                Volume(74.0157)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Cembalo\nContinuo')
            PartAbbreviation('CEM\nB.C.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(3)
                MidiProgram(7)
                Volume(59.8425)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Viola da\nGamba\nContinuo')
            PartAbbreviation('VDG\nB.C.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(4)
                MidiProgram(43)
                Volume(51.9685)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=503.46):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(117.39)
                        RightMargin(0.0)
                    TopSystemDistance(903.78)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                Instruments(2)
                with Clef():
                    Sign('C')
                    Line(4)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('60', default_x=-43.12, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Attributes():
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Evangelista', default_y=35.62, font_weight='bold', font_size='12')
            with Note(default_x=198.73, default_y=5.0, dynamics=120.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Si')
            with Note(default_x=249.25, default_y=5.0, dynamics=120.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('mon')
            with Note(default_x=299.77, default_y=20.0, dynamics=120.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Pe')
            with Note(default_x=350.29, default_y=20.0, dynamics=120.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('trus')
            with Note(default_x=400.81, default_y=20.0, dynamics=120.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=451.33, default_y=25.0, dynamics=120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ber')
        with Measure(number='2', width=516.29):
            with Note(default_x=17.82, default_y=30.0, dynamics=120.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fol')
            with Note(default_x=76.27, default_y=30.0, dynamics=120.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=112.81, default_y=35.0, dynamics=120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
            with Note(default_x=149.34, default_y=40.0, dynamics=120.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=207.8, default_y=30.0, dynamics=120.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('su')
            with Direction(placement='above'):
                with DirectionType():
                    Words('18', default_y=35.82, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=18.0)
            with Note(default_x=266.26, default_y=45.0, dynamics=120.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('nach')
            with Direction(placement='above'):
                with DirectionType():
                    Words('54', default_y=0.82, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=54.0)
            with Note(default_x=324.71, default_y=10.0, dynamics=120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=361.25, default_y=25.0, dynamics=120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Note(default_x=397.78, default_y=15.0, dynamics=120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an')
            with Note(default_x=456.24, default_y=20.0, dynamics=120.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
        with Measure(number='3', width=331.12):
            with Note(default_x=20.42, default_y=20.0, dynamics=120.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jün')
            with Note(default_x=68.95, default_y=5.0, dynamics=120.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ger')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=503.46):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(83.4)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=114.57, default_y=-193.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=114.57, default_y=-178.4):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=114.57, default_y=-168.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=114.57, default_y=-248.4, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=516.29):
            with Note(default_x=17.46, default_y=-193.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.46, default_y=-178.4):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.46, default_y=-168.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=266.26, default_y=-178.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=278.12, default_y=-173.4):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=266.26, default_y=-163.4):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=266.26, default_y=-153.4):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.46, default_y=-248.4, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=265.89, default_y=-243.4, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=331.12):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=117.48, default_y=-178.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.48, default_y=-168.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=117.48, default_y=-158.4):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=117.48, default_y=-143.4):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=166.01, default_y=-173.4):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=166.01, default_y=-163.4):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=177.88, default_y=-158.4):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=166.01, default_y=-148.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=214.19, default_y=-168.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=214.19, default_y=-158.4):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=214.19, default_y=-143.4):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=117.48, default_y=-238.4, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=214.19, default_y=-258.4, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=503.46):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=114.57, default_y=-353.4, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=516.29):
            with Note(default_x=17.46, default_y=-353.4, dynamics=111.11):
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
            with Note(default_x=265.89, default_y=-348.4, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=331.12):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=117.48, default_y=-343.4, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=214.19, default_y=-363.4, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')