with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 21 ')
        WorkTitle('Cantata "Ich hatte viel bekümmernis in meinem Herzen"')
    MovementNumber('4')
    MovementTitle('Seufze, Tränen, Kümmer, Not')
    with Identification():
        Creator('Edward J Maurath', type='arranger')
        Creator('Johann Sebastian Bach', type='composer')
        Rights('Sequenced by Edward J Maurath')
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
        CreditWords('Seufze, Tränen, Kümmer, Not', default_x=611.961, default_y=1527.21, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Bach: Cantata #21, Aria in c minor\n', default_x=611.961, default_y=1470.52, justify='center', valign='top', font_family='Times New Roman', font_size='14')
        CreditWords('More at http://bach.ejmaurath.com')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1167.23, default_y=1361.91, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Sequenced by Edward J. Maurath', default_x=56.6893, default_y=1361.91, justify='left', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Sequenced by Edward J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Sequenced by Edward J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Oboe')
            PartAbbreviation('OBO')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(69)
                Volume(65.3543)
                Pan(-47.0)
        with ScorePart(id='P2'):
            PartName('Soprano')
            PartAbbreviation('SOP')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(74)
                Volume(100.0)
                Pan(34.0)
        with ScorePart(id='P3'):
            PartName('Organo\n(Continuo)')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Hpsi RH')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(75)
                Volume(34.6457)
                Pan(-90.0)
        with ScorePart(id='P4'):
            PartName('Bassoon\n(Continuo)')
            PartAbbreviation('BSN')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Continuo')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(71)
                Volume(66.1417)
                Pan(90.0)
    with Part(id='P1'):
        with Measure(number='1', width=388.96):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(111.99)
                        RightMargin(-0.0)
                    TopSystemDistance(245.3)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('42', default_x=-47.49, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=42.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=186.76, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=208.28, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=236.44, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=257.96, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.39, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=313.91, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=335.43, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=365.79, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=326.33):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.67, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.28, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=98.66, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.83, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=152.21, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=177.6, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=218.21, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.58, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.96, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=299.35, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=283.26):
            with Note(default_x=15.8, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.98, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=72.97, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.96, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=116.95, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=138.94, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.93, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=182.92, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=204.91, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=226.89, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=248.88, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=449.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.32, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.84, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=149.37, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=176.15, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.67, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=227.2, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=253.98, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=279.5, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=305.03, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=326.0, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=350.76, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=371.73, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=397.26, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=422.78, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=306.14):
            with Note(default_x=16.2, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=55.06, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.35, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.51, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=131.8, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=156.09, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=194.95, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=221.72, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=249.89, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=280.26, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=296.09):
            with Note(default_x=12.0, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.64, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=75.41, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.31, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.21, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.37, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=172.27, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=195.17, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=218.06, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=240.96, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=271.33, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=418.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=107.12, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.55, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=172.83, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=198.1, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=223.37, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=251.54, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=276.81, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=302.09, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=328.86, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=354.14, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=379.41, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='8', width=326.57):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=41.7)
            with Note(default_x=15.8, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
        with Measure(number='9', width=307.19):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=85.54, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.01, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=138.18, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=162.65, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.81, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=226.28, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=250.76, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=281.12, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=409.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=98.32, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.61, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=325.65, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=353.82, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=380.88, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=290.65):
            with Note(default_x=15.8, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.91, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=218.38, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=241.93, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=265.49, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=351.96):
            with Note(default_x=15.8, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.29, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=96.04, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.78, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=149.53, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.27, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.02, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=229.76, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=256.51, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=256.51, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=283.26, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=317.59, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='13', width=677.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.32, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=135.43, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.54, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=209.66, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=246.77, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=283.89, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=321.0, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=358.11, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=395.23, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=424.39, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=449.15, default_y=15.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=470.36, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=507.48, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=565.8, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=374.16):
            with Note(default_x=16.2, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=67.11, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=194.38, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=245.29, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='15', width=404.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.32, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.05, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=167.77, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.93, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=222.64, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=249.36, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.1, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=318.87, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=345.58, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=375.95, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=293.75):
            with Note(default_x=14.0, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.63, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=215.7, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=243.86, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=268.01, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=354.14):
            with Note(default_x=12.12, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.27, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=264.9, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=296.29, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=324.46, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=369.14):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=98.43, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=143.13, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=304.5):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=85.86, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=109.93, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=141.33, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.4, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=203.91, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=230.69, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=254.76, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=278.83, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=378.51):
            with Note(default_x=12.0, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.48, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=95.05, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.06, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=158.22, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=188.38, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=218.55, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=248.71, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=278.88, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=309.04, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=346.74, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=474.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.32, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.55, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=152.78, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=180.01, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=211.4, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=238.63, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=276.41, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=303.64, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=330.87, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=350.67, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=367.84, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=385.0, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=413.17, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=440.4, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=270.35):
            with Note(default_x=14.0, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=68.5, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=89.46, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=110.42, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=140.78, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=161.74, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=182.7, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=203.66, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=224.62, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=245.58, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=307.02):
            with Note(default_x=14.0, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.25, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.02, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.3, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.59, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=152.75, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=176.03, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=199.31, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=226.09, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=249.37, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=272.65, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=649.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.4)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=102.12, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=224.5, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.57, default_y=-5.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=318.63, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=365.7, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=441.01, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=488.08, default_y=10.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=535.15, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=582.22, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=402.19):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=61.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('44')
                Sound(tempo=44.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(64.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('?')
                    DisplayOctave(-31)
                Duration(64.0)
                Voice('4')
                Type('whole')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Offset(-80.0)
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('39')
                Sound(tempo=39.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')
    with Part(id='P2'):
        with Measure(number='1', width=388.96):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('C')
                    Line(1)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=326.33):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=283.26):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=449.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=306.14):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=296.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=418.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='8', width=326.57):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=41.7)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.56, default_y=-90.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.48, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=147.64, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=173.56, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=215.04, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=240.96, default_y=-85.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=266.88, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=299.05, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=307.19):
            with Note(default_x=12.12, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.07, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=162.65, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.81, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=409.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.32, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.61, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=173.01, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.17, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=228.24, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=255.3, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=298.59, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=290.65):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=86.47, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.02, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=133.58, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=157.13, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=194.82, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=351.96):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=96.04, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.78, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=149.53, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.27, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.02, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=229.76, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=256.51, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=283.26, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=300.42, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=317.59, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=677.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.32, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=209.66, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=246.77, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=283.89, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=321.0, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=358.11, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=395.23, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=470.36, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=507.48, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=536.64, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=565.8, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=374.16):
            with Note(default_x=16.2, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.93, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.74, default_y=-90.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=162.56, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=194.38, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=245.29, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=277.11, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=308.93, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=340.74, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=404.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.32, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.05, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=249.36, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.1, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=293.75):
            with Note(default_x=14.0, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=79.04, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.19, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=127.33, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=151.47, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.1, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=354.14):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=96.35, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=124.51, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=152.59, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=180.67, default_y=-135.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=208.74, default_y=-140.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=369.14):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=165.48, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=187.83, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=219.22, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=241.57, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=277.33, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=299.68, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=322.02, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=344.37, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=304.5):
            with Note(default_x=12.12, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.26, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=109.93, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.33, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.4, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=203.91, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=254.76, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.83, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=378.51):
            with Note(default_x=12.0, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.48, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=95.05, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.06, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=158.22, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=188.38, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=218.55, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=248.71, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=278.88, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=309.04, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.89, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=346.74, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=474.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.32, default_y=-115.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.01, default_y=-120.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=211.4, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=238.63, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=276.41, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=303.64, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=330.87, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=385.0, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=413.17, default_y=-130.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=440.4, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=270.35):
            with Note(default_x=14.0, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=140.78, default_y=-85.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=182.7, default_y=-90.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=307.02):
            with Note(default_x=14.0, default_y=-95.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.25, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=152.75, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=199.31, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=249.37, default_y=-125.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=272.65, default_y=-100.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=649.96):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=102.12, default_y=-105.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=177.43, default_y=-110.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=402.19):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=61.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')
    with Part(id='P3'):
        with Measure(number='1', width=388.96):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=186.76, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=186.76, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=257.96, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=313.91, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=326.33):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.67, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.66, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.66, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.6, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.58, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=248.58, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=283.26):
            with Note(default_x=15.8, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=72.97, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.97, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.94, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=138.94, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=204.91, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=449.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.32, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.32, default_y=-40.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.15, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=253.98, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.98, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=371.73, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=371.73, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=306.14):
            with Note(default_x=16.2, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=79.35, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.35, default_y=-40.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=79.35, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.09, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.72, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=221.72, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=296.09):
            with Note(default_x=12.0, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=75.41, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=149.37, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.37, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.06, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.06, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=418.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=107.12, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.12, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.12, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=251.54, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=328.86, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=328.86, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=379.41, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=379.41, default_y=-55.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=379.41, default_y=-45.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='8', width=326.57):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=41.7)
            with Note(default_x=15.8, default_y=-75.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-65.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-50.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=93.56, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.56, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.56, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=173.56, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=240.96, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=240.96, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=307.19):
            with Note(default_x=12.12, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=85.54, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=85.54, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=162.65, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=226.28, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=409.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.32, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.32, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.01, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=255.3, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=255.3, default_y=-50.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=255.3, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=325.65, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=325.65, default_y=-50.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=325.65, default_y=-40.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=325.65, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=290.65):
            with Note(default_x=15.8, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-50.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=86.47, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.47, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.13, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.38, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=218.38, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='12', width=351.96):
            with Note(default_x=15.8, default_y=-40.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.04, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.27, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=256.51, default_y=-20.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='13', width=677.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.32, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.32, default_y=-40.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=209.66, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=321.0, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=321.0, default_y=-45.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=470.36, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=374.16):
            with Note(default_x=16.2, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.93, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.93, default_y=-40.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=98.93, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=194.38, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=194.38, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=277.11, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=277.11, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='15', width=404.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.32, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=167.77, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.77, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=249.36, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=318.87, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=318.87, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=293.75):
            with Note(default_x=14.0, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=79.04, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.04, default_y=-55.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=79.04, default_y=-45.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=151.47, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=215.7, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='17', width=354.14):
            with Note(default_x=12.12, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.35, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.35, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=264.9, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=276.76, default_y=-60.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='18', width=369.14):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.43, default_y=-65.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.48, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=165.48, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Note(default_x=299.68, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=299.68, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='19', width=304.5):
            with Note(default_x=12.12, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.12, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=85.86, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=85.86, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.4, default_y=-60.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=165.4, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='20', width=378.51):
            with Note(default_x=12.0, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
        with Measure(number='21', width=474.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=98.32, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.01, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=180.01, default_y=-25.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=276.41, default_y=-50.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=276.41, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=385.0, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=385.0, default_y=-30.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='22', width=270.35):
            with Note(default_x=14.0, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=14.0, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=68.5, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.5, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.5, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=140.78, default_y=-55.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=140.78, default_y=-35.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=140.78, default_y=-10.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=203.66, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=307.02):
            with Note(default_x=14.0, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=78.02, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.02, default_y=-20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.75, default_y=-35.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=226.09, default_y=-45.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=649.96):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=102.12, default_y=-75.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=102.12, default_y=-65.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=224.5, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=224.5, default_y=-5.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=365.7, default_y=-15.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=488.08, default_y=-25.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=402.19):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=61.0)
            with Note(default_x=15.8, default_y=-75.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-65.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=15.8, default_y=-50.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')
    with Part(id='P4'):
        with Measure(number='1', width=388.96):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=186.76, default_y=-200.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=257.96, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=313.91, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=326.33):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.67, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.66, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.6, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.58, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=283.26):
            with Note(default_x=15.8, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=72.97, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.95, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=138.94, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=182.92, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=204.91, default_y=-205.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=248.88, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=449.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.32, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.37, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=176.15, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=227.2, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=253.98, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=305.03, default_y=-260.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=371.73, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=422.78, default_y=-205.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='5', width=306.14):
            with Note(default_x=16.2, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=79.35, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.09, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=221.72, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=296.09):
            with Note(default_x=12.0, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=75.41, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.21, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=149.37, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.17, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=218.06, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=271.33, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='7', width=418.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=107.12, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=223.37, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=251.54, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=302.09, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=328.86, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=379.41, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='8', width=326.57):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=41.7)
            with Note(default_x=15.8, default_y=-270.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=93.56, default_y=-200.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.56, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=240.96, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=307.19):
            with Note(default_x=12.12, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=85.54, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=162.65, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=226.28, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=409.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.32, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.01, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=255.3, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=325.65, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=290.65):
            with Note(default_x=15.8, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=86.47, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.13, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.38, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='12', width=351.96):
            with Note(default_x=15.8, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.04, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.53, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=176.27, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=229.76, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=256.51, default_y=-205.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=317.59, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=677.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.32, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=172.54, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=209.66, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=283.89, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=321.0, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=395.23, default_y=-260.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=470.36, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=565.8, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=565.8, default_y=-205.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=596.12, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=596.12, default_y=-205.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('32nd')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=626.45, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('begin', number=4)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=626.45, default_y=-205.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('64th')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=653.22, default_y=-205.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                with Notations():
                    Tied(type='stop')
        with Measure(number='14', width=374.16):
            with Note(default_x=16.2, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.93, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=194.38, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=277.11, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='15', width=404.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.32, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=167.77, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=249.36, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=318.87, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=293.75):
            with Note(default_x=14.0, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=79.04, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=151.47, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=215.7, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='17', width=354.14):
            with Note(default_x=12.12, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.35, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.67, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=264.9, default_y=-265.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='18', width=369.14):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.43, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.48, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=241.57, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=299.68, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='19', width=304.5):
            with Note(default_x=12.12, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=85.86, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.4, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=230.69, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='20', width=378.51):
            with Note(default_x=12.0, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=95.05, default_y=-200.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.22, default_y=-205.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=188.38, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=248.71, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=278.88, default_y=-195.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=346.74, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='21', width=474.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=98.32, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=152.78, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=180.01, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.63, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=276.41, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=330.87, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=385.0, default_y=-230.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=440.4, default_y=-265.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='22', width=270.35):
            with Note(default_x=14.0, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=68.5, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=110.42, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=140.78, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=182.7, default_y=-225.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=203.66, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=245.58, default_y=-215.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=307.02):
            with Note(default_x=14.0, default_y=-240.0, dynamics=88.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=51.25, default_y=-235.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=78.02, default_y=-245.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=124.59, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=152.75, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=199.31, default_y=-260.0, dynamics=88.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=226.09, default_y=-255.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=272.65, default_y=-250.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='24', width=649.96):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=102.12, default_y=-270.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=224.5, default_y=-200.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=365.7, default_y=-210.0, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=488.08, default_y=-220.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=402.19):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=61.0)
            with Note(default_x=15.8, default_y=-270.0, dynamics=88.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='discontinue')