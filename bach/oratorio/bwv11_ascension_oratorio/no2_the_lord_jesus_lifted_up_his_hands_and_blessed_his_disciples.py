with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 11')
        WorkTitle('Ascension Oratorio')
    MovementNumber('#2')
    MovementTitle('Der HErr Jesu hub seine Hände auf und segnete seine Jünger')
    with Identification():
        Creator('Johann Sebastian Bach, 1735', type='composer')
        Creator('Martin Luther', type='lyricist')
        Rights('Sequenced by Edward James Maurath')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1583.9)
            PageWidth(1223.92)
            with PageMargins(type='both'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Der Herr Jesu hub seine Hände auf\n', default_x=611.961, default_y=1527.21, justify='center', valign='top', font_size='24')
        CreditWords('und segnete seine Jünger')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('\n', default_x=611.961, default_y=1470.52, justify='center', valign='top', font_size='14')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('BWV 11 #2 Recitativo secco for Evangelium\n')
        CreditWords('More Bach at http://bach.ejmaurath.com/\n')
        CreditWords('Uploaded from Musescore 2')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach, 1735\n', default_x=1167.23, default_y=832.66, justify='right', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Martin Luther\n', default_x=56.6893, default_y=832.66, justify='left', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward James Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Evangelium')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(5)
                Volume(100.0)
                Pan(7.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P2'):
            PartName('Bassoon\nContinuo')
            PartAbbreviation('BSN')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(71)
                Volume(29.9213)
                Pan(9.0)
        with ScorePart(id='P3'):
            PartName('Violoncello\nContinuo')
            PartAbbreviation('VCL')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(43)
                Volume(28.3465)
                Pan(90.0)
        with ScorePart(id='P4'):
            PartName('Contrabasso\nContinuo')
            PartAbbreviation('CTB')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(44)
                Volume(37.0079)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P5'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(33)
                Volume(100.0)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P6'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(33)
                Volume(100.0)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Cembalo\nContinuo')
            PartAbbreviation('CEM')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(7)
                MidiProgram(7)
                Volume(39.3701)
                Pan(-90.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=349.82):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(123.19)
                        RightMargin(-0.0)
                    TopSystemDistance(764.55)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('60', default_x=-39.32, relative_y=9.4, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=155.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=185.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=215.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=245.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=276.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=306.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=325.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=285.79):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=128.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=148.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=180.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=252.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=239.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=276.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=313.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(56.4)
                        RightMargin(-0.0)
                    SystemDistance(266.35)
            with Note(default_x=89.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=168.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=201.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=246.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=291.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=344.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=376.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=327.76):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=53.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=136.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=218.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=202.25):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(87.93)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Hidden Continuo by\n', relative_x=-65.79, relative_y=56.83)
                    Words('Edward James Maurath')
            with Note(default_x=110.67, default_y=-157.93):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-157.93):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.92, default_y=-162.93):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-157.93):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=85.83, default_y=-157.93):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.57, default_y=-152.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=135.35, default_y=-147.93):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=152.13, default_y=-142.93):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=168.91, default_y=-137.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=185.69, default_y=-132.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=202.11, default_y=-127.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=89.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=376.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=417.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=437.66, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=458.23, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=478.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=499.37, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=260.04, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-167.93)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=110.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.92, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=85.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=118.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
            with Note(default_x=135.35, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=152.13, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=168.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=185.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=202.11, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=89.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=376.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
            with Note(default_x=417.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=437.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=458.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=478.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=499.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=260.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note(default_x=110.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.92, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=85.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=118.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
            with Note(default_x=135.35, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=152.13, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=168.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=185.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=202.11, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=89.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=376.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
            with Note(default_x=417.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=437.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=458.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=478.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=499.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=260.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=110.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.92, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=85.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
            with Note(default_x=118.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
            with Note(default_x=135.35, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=152.13, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=168.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=185.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=202.11, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=89.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=376.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
            with Note(default_x=417.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=437.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=458.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=478.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
            with Note(default_x=499.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=260.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=110.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note(default_x=110.67, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note(default_x=110.67, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note(default_x=110.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.92, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.92, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=147.92, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=202.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=202.11, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=202.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=214.7, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=89.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.61, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.61, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.2, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=303.43, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=291.57, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=291.57, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.12, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=23.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.63, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.76, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=260.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=260.04, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=260.04, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=326.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=338.02, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=326.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Note(default_x=12.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=349.82):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
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
            with Note(default_x=110.67, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-39.49)
            with Note(default_x=110.67, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-39.49)
            with Note(default_x=110.67, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-39.49)
            with Backup():
                Duration(32.0)
            with Note(default_x=110.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=285.79):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-18.53, default_y=-34.55)
            with Note(default_x=12.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-18.53, default_y=-34.55)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-18.53, default_y=-34.55)
            with Note(default_x=147.92, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-29.55)
            with Note(default_x=147.92, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-29.55)
            with Note(default_x=147.92, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-29.55)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.92, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=351.74):
            with Note(default_x=12.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-39.49)
            with Note(default_x=12.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-39.49)
            with Note(default_x=12.0, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-39.49)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=202.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=202.11, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=202.11, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=202.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=118.57, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=135.35, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=152.13, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=168.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=185.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=202.11, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=524.14):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=89.61, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=89.61, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=89.61, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=89.61, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-36.57, default_y=-19.55)
            with Note(default_x=291.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-32.04, default_y=-14.49)
            with Note(default_x=291.57, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-32.04, default_y=-14.49)
            with Note(default_x=303.43, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-32.04, default_y=-14.49)
            with Note(default_x=291.57, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-32.04, default_y=-14.49)
            with Note(default_x=291.57, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-32.04, default_y=-14.49)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=376.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=417.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=437.66, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=458.23, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=478.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=499.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=327.76):
            with Note(default_x=12.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-34.49)
            with Note(default_x=23.98, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-34.49)
            with Note(default_x=12.12, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-34.49)
            with Note(default_x=12.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-17.81, default_y=-34.49)
            with Note(default_x=94.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-35.84, default_y=-39.49)
            with Note(default_x=94.76, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-35.84, default_y=-39.49)
            with Note(default_x=94.76, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-35.84, default_y=-39.49)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=260.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=260.04, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=260.04, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=326.16, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=326.16, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=338.02, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=326.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.12, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=94.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=260.04, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=202.25):
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-19.49)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-19.49)
            with Note(default_x=12.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(direction='up', default_x=-24.45, default_y=-19.49)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')