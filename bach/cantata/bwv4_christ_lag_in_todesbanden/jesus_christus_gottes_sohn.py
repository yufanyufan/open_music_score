with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 4 Versus 3')
        WorkTitle('Cantata "Christ lag in Todesbanden"')
    MovementNumber('Versus 3 (4th mvt)')
    with Identification():
        Creator('Edward J Maurath', type='arranger')
        Creator('Johann Sebastian Bach (1685--1750)', type='composer')
        Creator('Martin Luthor', type='lyricist')
        Rights('Sequenced by Edwarard J Maurath')
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
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)', default_x=1167.23, default_y=1301.48, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('title')
        CreditWords('"Jesus Christus, Gottes Sohn" Versus 3 for Tenor', default_x=611.961, default_y=1527.21, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords("BWV 4 Cantata 'Christ lag in Todesbanden (1725)\n", default_x=611.961, default_y=1470.52, justify='center', valign='top', font_size='14')
        CreditWords("More at http://bach.ejmaurath.com'")
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Martin Luther', default_x=56.6893, default_y=1301.48, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edwarard J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Sequenced by Edwarard J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Sequenced by Edwarard J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Sequenced by Edwarard J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('Sequenced by Edwarard J Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Violin')
            PartAbbreviation('VLN')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violins')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(49)
                Volume(81.8898)
                Pan(-53.0)
        with ScorePart(id='P2'):
            PartName('Tenor')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(71)
                Volume(81.8898)
                Pan(41.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P3'):
            PartName('Cembalo\n(Continuo)')
            PartAbbreviation('CEM')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Hpsi RH')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(39)
                Volume(47.2441)
                Pan(-90.0)
        with ScorePart(id='P4'):
            PartName('Cembalo\n(Continuo)')
            PartAbbreviation('CEM')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Hpsi LH')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(39)
                Volume(46.4567)
                Pan(-90.0)
        PartGroup(type='stop', number='1')
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P5'):
            PartName('Violoncello\n(Continuo)')
            PartAbbreviation('VCL')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Continuo')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(49)
                Volume(39.3701)
                Pan(90.0)
        with ScorePart(id='P6'):
            PartName('Contrabass\n(Continuo)')
            PartAbbreviation('CTB')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Contrabass')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(49)
                Volume(41.7323)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=275.1):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(119.19)
                        RightMargin(-0.0)
                    TopSystemDistance(305.73)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('72', default_x=-37.06, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=72.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=120.88, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.27, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.89, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=191.5, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.11, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.73, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.34, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=171.29):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.22, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.44, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.65, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.87, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.09, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.31, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.53, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=171.29):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.22, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.44, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.65, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.87, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.09, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.31, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.53, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=171.29):
            with Note(default_x=12.0, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.22, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.44, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.65, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.87, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.09, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.31, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.53, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=202.37):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.18, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.95, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.71, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.9, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.08, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.84, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.61, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(144.05)
            with Note(default_x=79.15, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.54, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.92, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.31, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.71, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.09, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.48, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.86, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=187.16):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.88, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.84, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.81, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.46, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.1, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.75, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.39, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=188.71):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.09, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.18, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.27, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.36, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.46, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.55, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.94, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=203.76):
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.53, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.92, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.65, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.37, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.1, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.27, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.99, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.97, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.37, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.77, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.51, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.25, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.99, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.73, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(144.05)
            with Note(default_x=79.15, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.9, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.66, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.43, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.18, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.93, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.69, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.46, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.49, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.99, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.48, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.97, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.47, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.96, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.36, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.39, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.72, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.89, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.05, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.81, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.58, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=198.9):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.79, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.58, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.37, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.76, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.55, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.34, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=189.58):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.31, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.4, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.48, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.64, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.73, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.81, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.09, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.37, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.66, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.95, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=165.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.52, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.81, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.2, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.93, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.33, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.27, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.2, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.13, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.07, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.29, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.57, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.97, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.26, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.54, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.83, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.12, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.29, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.57, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.86, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.26, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.54, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.83, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.12, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=196.24):
            with Note(default_x=12.36, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.65, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.93, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.22, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.51, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.79, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.48, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(126.28)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.5, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.86, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.56, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.92, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.27, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.62, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=186.24):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.35, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.71, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.06, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.41, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.77, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.12, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.47, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=186.24):
            with Note(default_x=12.0, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.35, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.71, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.06, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.41, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.77, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.12, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.47, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=217.32):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.47, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.93, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.4, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.33, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.79, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.26, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=208.56):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.37, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.73, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.1, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.5, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.86, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.23, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.59, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(126.28)
            with Note(default_x=91.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.33, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.29, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.26, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.4, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.54, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.67, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.81, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=186.17):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.67, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.33, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.67, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.34, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.4, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=198.35):
            with Note(default_x=12.94, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.15, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.55, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.77, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.99, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.2, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.37, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.59, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.46, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.86, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.26, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.49, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.72, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.95, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.18, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.29, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.06, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.82, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.11, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.4, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.17, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.93, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(126.28)
            with Note(default_x=79.15, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.79, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.43, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.07, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=165.72, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.36, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.0, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.4, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.77, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.31, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.85, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.94, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.7, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.47, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=198.01):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.64, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.28, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.92, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.32, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.96, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.61, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.25, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=199.94):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.86, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.49, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.12, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.75, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.38, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.54, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.17, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=184.4):
            with Note(default_x=12.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.89, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.85, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.81, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.76, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.72, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.68, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.63, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.06, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.46, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.37, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.29, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.2, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.11, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.03, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.4, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.8, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.19, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.59, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.99, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.39, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.56, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.27, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.8, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.19, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.46, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.73, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.99, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.87, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.5, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.13, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.77, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.4, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.04, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.67, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=181.21):
            with Note(default_x=12.0, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.63, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.27, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.9, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.54, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.17, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.81, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.44, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(251.47)
            with Note(default_x=79.15, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=97.08, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.02, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.95, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.88, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.82, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.58, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.35, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=182.74):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.16, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.33, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.49, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.88, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.05, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.01, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.98, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=173.42):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.1, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.06, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.96, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.86, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.76, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.66, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=174.97):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.7, relative_y=-40.0):
                        F()
                Sound(dynamics=115.56)
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.8, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.6, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.41, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.01, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.81, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.21, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=187.28):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=31.03, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.43, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.41, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.39, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.37, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.53, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.51, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(251.47)
            with Note(default_x=79.15, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.06, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.46, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.37, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.29, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.2, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.21, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.17, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.34, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.34, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.34, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.7, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                Sound(tempo=71.0)
            with Note(default_x=89.45, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=89.45, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=89.45, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=125.57, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='49', width=166.96):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.91, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=88.02, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=88.02, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=124.14, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=124.14, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=124.14, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='50', width=182.94):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Sound(tempo=68.0)
            with Note(default_x=5.37, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=17.23, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=66.89, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.29, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Sound(tempo=67.0)
            with Note(default_x=103.4, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.4, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=139.92, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=139.92, default_y=-15.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='51', width=163.16):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=48.11, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=48.11, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Sound(tempo=65.0)
            with Note(default_x=84.22, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.22, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=120.34, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.34, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='52', width=105.37):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('44')
                Sound(tempo=44.0)
            with Note(default_x=15.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=140.06, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=14.0, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('32nd')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=44.33, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('begin', number=4)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=44.33, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('64th')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=74.65, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('128th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                Beam('forward hook', number=5)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=74.65, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('128th')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=104.98, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=130.14, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('128th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
                Beam('forward hook', number=4)
                Beam('forward hook', number=5)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.3, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.7, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.88, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.28, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.67, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=168.98, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='56', width=200.74):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Sound(tempo=72.0)
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.89, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.78, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.66, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.55, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.44, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.21, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.97, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='57', width=199.75):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.93, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.86, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.79, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.19, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.12, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.05, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.98, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(261.92)
            with Note(default_x=91.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.51, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.83, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.15, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.47, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.8, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.28, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='59', width=187.61):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.55, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.1, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.65, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.2, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.75, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.3, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.84, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='60', width=188.55):
            with Note(default_x=12.94, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.49, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.04, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.59, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.13, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.68, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.23, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.78, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.66, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.32, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.98, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.64, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.3, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.96, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.62, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.33, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.67, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.33, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.67, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.06, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.4, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(261.92)
            with Note(default_x=79.15, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.03, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.91, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.79, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.67, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=201.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.33, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.21, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.82, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.84, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.85, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.87, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.89, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.29, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.3, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='65', width=179.72):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.42, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.84, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.27, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.69, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.11, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.53, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.95, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='66', width=200.49):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.02, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.82, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.61, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.2, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.96, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.73, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='67', width=191.49):
            with Note(default_x=12.12, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.21, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.29, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.38, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.47, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.55, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.64, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.73, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=79.27, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.01, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=112.01, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=152.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.94, default_y=10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=193.86, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=193.86, default_y=15.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.4, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.4, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=103.01, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.01, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=146.61, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=146.61, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.8, default_y=10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=48.81, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.81, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=77.67, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.53, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.39, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.25, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.02, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.88, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.36, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.71, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.07, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.43, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.14, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.5, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=172.88):
            with Note(default_x=13.06, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.98, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.91, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.65, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(161.28)
            with Note(default_x=79.15, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.61, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.07, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.53, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.98, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.44, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.9, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.3, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.8, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.59, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.99, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.78, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.58, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.74, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.54, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=38.19, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=59.14, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.09, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.05, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.95, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.26, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.66, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.11, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.57, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.03, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.49, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.95, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='77', width=182.36):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.8, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.6, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.4, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.2, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.8, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.6, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(161.28)
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.13, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.11, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.1, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.08, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=184.06, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.04, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.02, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='79', width=183.64):
            with Note(default_x=12.0, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.98, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.96, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.95, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.93, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.91, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.89, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.87, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='80', width=214.72):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.14, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.28, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.42, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.56, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.7, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.84, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.98, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='81', width=205.96):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.97, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.93, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.9, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.3, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.26, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.23, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.19, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='82', width=196.64):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.32, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.41, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.51, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.6, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.69, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.78, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.87, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(58.8)
                        RightMargin(-0.0)
                    SystemDistance(161.28)
            with Note(default_x=79.15, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.74, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.43, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=404.11, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=517.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('48')
                Sound(tempo=48.0)
            with Note(default_x=615.39, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=712.98, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=826.67, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                Offset(-62.0)
                Sound(tempo=71.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Offset(-60.0)
                Sound(tempo=70.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Offset(-59.0)
                Sound(tempo=69.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Offset(-57.0)
                Sound(tempo=68.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Offset(-55.0)
                Sound(tempo=67.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Offset(-54.0)
                Sound(tempo=66.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Offset(-52.0)
                Sound(tempo=65.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Offset(-50.0)
                Sound(tempo=64.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Offset(-49.0)
                Sound(tempo=63.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Offset(-47.0)
                Sound(tempo=62.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('61')
                Offset(-45.0)
                Sound(tempo=61.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Offset(-44.0)
                Sound(tempo=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('59')
                Offset(-42.0)
                Sound(tempo=59.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('58')
                Offset(-40.0)
                Sound(tempo=58.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('57')
                Offset(-39.0)
                Sound(tempo=57.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('56')
                Offset(-37.0)
                Sound(tempo=56.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Offset(-35.0)
                Sound(tempo=55.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('54')
                Offset(-34.0)
                Sound(tempo=54.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('53')
                Offset(-32.0)
                Sound(tempo=53.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('52')
                Offset(-30.0)
                Sound(tempo=52.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('51')
                Offset(-29.0)
                Sound(tempo=51.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Offset(-27.0)
                Sound(tempo=50.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('49')
                Offset(-25.0)
                Sound(tempo=49.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('47')
                Offset(-22.0)
                Sound(tempo=47.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('46')
                Offset(-20.0)
                Sound(tempo=46.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('45')
                Offset(-19.0)
                Sound(tempo=45.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('44')
                Offset(-17.0)
                Sound(tempo=44.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('43')
                Offset(-15.0)
                Sound(tempo=43.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('42')
                Offset(-14.0)
                Sound(tempo=42.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('41')
                Offset(-12.0)
                Sound(tempo=41.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Offset(-10.0)
                Sound(tempo=40.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('39')
                Offset(-9.0)
                Sound(tempo=39.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('38')
                Offset(-7.0)
                Sound(tempo=38.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('37')
                Offset(-5.0)
                Sound(tempo=37.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('36')
                Offset(-4.0)
                Sound(tempo=36.0)
        with Measure(number='84', width=140.51):
            with Note(default_x=15.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=275.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(4)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='2', width=171.29):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='3', width=171.29):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=171.29):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=202.37):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='7', width=187.16):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='8', width=188.71):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='9', width=203.76):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=109.37, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=121.51, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.99, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=176.18, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.97, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=198.9):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='15', width=189.58):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=165.23, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.2, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.26, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=196.24):
            with Note(default_x=12.0, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(64.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='22', width=186.24):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='23', width=186.24):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='24', width=217.32):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=208.56):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='27', width=186.17):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='28', width=198.35):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=104.99, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=120.49, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.95, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=106.11, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=165.72, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=198.01):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='34', width=199.94):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='35', width=184.4):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=96.76, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.29, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.59, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.53, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.19, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='40', width=181.21):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.9)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='42', width=182.74):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='43', width=173.42):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='44', width=174.97):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-160.9, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.63, default_y=-150.9, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='46', width=187.28):
            with Note(default_x=13.06, default_y=-145.9, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.39, default_y=-160.9, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.53, default_y=-155.9, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.29, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='49', width=166.96):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='50', width=182.94):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=103.4, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=163.16):
            with Note(default_x=12.0, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.22, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='52', width=105.37):
            with Note(default_x=15.8, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=80.6, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(64.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=234.41, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.81, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.28, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=110.67, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='56', width=200.74):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='57', width=199.75):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='59', width=187.61):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='60', width=188.55):
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=99.13, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.64, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.33, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.67, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=183.83, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=201.0, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=218.16, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=235.33, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='65', width=179.72):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='66', width=200.49):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='67', width=191.49):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=56.29, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.38, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.47, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.55, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.64, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.73, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.27, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=112.01, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.47, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.94, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.4, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.86, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.33, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.4, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.2, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.01, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.81, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.61, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.81, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.67, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.53, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.39, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.25, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.02, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.88, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.36, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.71, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.07, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.43, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.14, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.5, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=172.88):
            with Note(default_x=13.06, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.98, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.91, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.11, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=79.15, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=186.44, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.9, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.3, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=138.58, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.74, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.54, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.14, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.05, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=163.91, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=182.36):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='79', width=183.64):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='80', width=214.72):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='81', width=205.96):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='82', width=196.64):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
        with Measure(number='84', width=140.51):
            with Note():
                Rest(measure='yes')
                Duration(64.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=275.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=101.26, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.26, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.26, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.5, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=191.5, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=191.5, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=171.29):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=88.87, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=171.29):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=171.29):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.87, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=202.37):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.71, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=174.71, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.71, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=187.16):
            with Note(default_x=17.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.46, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.46, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=188.71):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.36, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=92.36, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=92.36, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=132.55, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=132.55, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=132.55, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='9', width=203.76):
            with Note(default_x=15.8, default_y=-75.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.37, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=121.51, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=162.99, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.18, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.97, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=198.9):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='15', width=189.58):
            with Note(default_x=17.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=165.23, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.2, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.26, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=196.24):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.15, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=121.86, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=164.56, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=207.27, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=186.24):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=97.41, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=97.41, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=140.12, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=186.24):
            with Note(default_x=12.0, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=54.71, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.41, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=217.32):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.86, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.86, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=164.79, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='25', width=208.56):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=58.73, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=113.5, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=160.23, default_y=-70.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=91.19, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=91.19, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=91.19, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.4, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=173.4, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=213.67, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=186.17):
            with Note(default_x=12.0, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.33, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.67, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
        with Measure(number='28', width=198.35):
            with Note(default_x=12.94, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.94, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.94, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=104.99, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=120.49, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.95, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=106.11, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=165.72, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.4, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=154.7, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=198.01):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=55.28, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.32, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.61, default_y=-70.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=199.94):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=103.75, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.75, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=153.54, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=184.4):
            with Note(default_x=12.94, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=54.85, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=96.76, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.68, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=132.46, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=176.29, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=176.29, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=220.11, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=66.8, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=121.59, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=121.59, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=168.39, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-60.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=54.53, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=54.53, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=107.19, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=107.19, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='40', width=181.21):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-165.9)
            with Note(default_x=79.15, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.88, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.88, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.88, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=182.74):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.88, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=97.88, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.88, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='43', width=173.42):
            with Note(default_x=17.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.96, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.96, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='44', width=174.97):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.21, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=83.21, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=83.21, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=118.81, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=118.81, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=118.81, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-75.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.63, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='46', width=187.28):
            with Note(default_x=13.06, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.39, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.29, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=167.29, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=53.34, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.34, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.34, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.34, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=89.45, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=89.45, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=89.45, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=89.45, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=89.45, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=125.57, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=125.57, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='49', width=166.96):
            with Note(default_x=15.8, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.91, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=51.91, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.02, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=88.02, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.02, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.02, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.14, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=124.14, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.14, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.14, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.14, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='50', width=182.94):
            with Note(default_x=17.23, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=29.1, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=29.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=17.23, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=66.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=66.89, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.4, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.4, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=103.4, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.4, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=139.92, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=139.92, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=139.92, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=139.92, default_y=-15.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='51', width=163.16):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=48.11, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.11, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.11, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=84.22, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=84.22, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=84.22, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=84.22, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=84.22, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.34, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=120.34, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.34, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.34, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.34, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='52', width=105.37):
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=80.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=80.6, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=80.6, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(64.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.15, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.15, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(64.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=14.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=203.86, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=203.86, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=110.67, default_y=-70.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=110.67, default_y=-50.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=110.67, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='56', width=200.74):
            with Note(default_x=12.0, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='57', width=199.75):
            with Note(default_x=12.0, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.19, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=109.19, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.19, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=91.19, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.19, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=91.19, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.47, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.47, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=187.61):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.2, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=98.2, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='60', width=188.55):
            with Note(default_x=12.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.13, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=102.64, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.33, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.67, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=183.83, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=201.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=218.16, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=235.33, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='65', width=179.72):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='66', width=200.49):
            with Note():
                Rest()
                Duration(64.0)
                Voice('1')
                Type('half')
        with Measure(number='67', width=191.49):
            with Note(default_x=12.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.12, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.29, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.38, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.47, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.55, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.64, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.73, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.27, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.27, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.27, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=112.01, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.47, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.94, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.4, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.86, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.33, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.4, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.2, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.01, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.81, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.61, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.81, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.67, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.53, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.39, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.25, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.02, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.88, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.36, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.71, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.07, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.43, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.14, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.5, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=172.88):
            with Note(default_x=13.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=13.06, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=13.06, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=53.98, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.91, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.11, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=186.44, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.9, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.3, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=138.58, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.74, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.54, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.14, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.05, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=163.91, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-75.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-65.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='77', width=182.36):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.2, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=95.2, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.08, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.08, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.08, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='79', width=183.64):
            with Note(default_x=12.0, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.93, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.93, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.93, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='80', width=214.72):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=205.96):
            with Note(default_x=12.0, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.3, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=112.3, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.3, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='82', width=196.64):
            with Note(default_x=17.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=17.23, default_y=-20.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.6, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.6, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=517.8, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=517.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=517.8, default_y=-30.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=712.98, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=712.98, default_y=-45.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=712.98, default_y=-35.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='84', width=140.51):
            with Note(default_x=15.8, default_y=-65.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-55.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=275.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=140.0)
            with Note(default_x=101.26, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.26, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.26, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.5, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.73, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=171.29):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=171.29):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.87, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=171.29):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=202.37):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.92, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=174.71, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=217.48, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=187.16):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.46, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.75, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=188.71):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.18, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.36, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=203.76):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.37, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.27, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.37, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.51, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.99, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.18, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=224.69, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.99, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.97, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.96, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.89, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.89, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=101.89, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=147.81, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=198.9):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=55.58, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.76, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.76, default_y=10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=152.34, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=189.58):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.56, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.56, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=143.73, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=80.09, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.09, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=122.66, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.33, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=109.2, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=153.07, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.83, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=196.24):
            with Note(default_x=12.36, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.51, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.19, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.86, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.56, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=207.27, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=186.24):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.41, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=186.24):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.71, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.41, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=217.32):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=164.79, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='25', width=208.56):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.73, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=113.5, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=173.4, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.67, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=186.17):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.33, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.67, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=198.35):
            with Note(default_x=12.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=104.99, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.37, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.86, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.49, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.95, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.11, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.17, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.43, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.72, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=209.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.4, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=107.4, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=154.7, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=198.01):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.28, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.32, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.61, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=199.94):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.75, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.75, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=153.54, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=184.4):
            with Note(default_x=12.94, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.85, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.76, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.68, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.46, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.29, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=220.11, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.8, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.59, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.39, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.53, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=141.04, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=141.04, default_y=5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='40', width=181.21):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=12.0, default_y=10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=53.27, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.27, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=94.54, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.54, default_y=25.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=135.81, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.81, default_y=-10.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=79.15, default_y=-5.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=193.58, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=193.58, default_y=15.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='42', width=182.74):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.33, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.88, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.01, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='43', width=173.42):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.96, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.76, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='44', width=174.97):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.6, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=29.82, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=47.63, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.45, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='46', width=187.28):
            with Note(default_x=13.06, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.43, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=98.39, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.39, default_y=0.0, dynamics=106.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=144.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.46, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.29, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.29, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.34, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.4, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.45, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.51, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.57, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.62, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=166.96):
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.86, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.91, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.97, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.02, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.08, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.14, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=182.94):
            with Note(default_x=17.23, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.63, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.89, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.14, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.4, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.66, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.92, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.17, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=163.16):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.06, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.11, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.17, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.22, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.28, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.34, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.39, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=105.37):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=140.06, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.3, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.86, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.41, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.88, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.67, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.55, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='56', width=200.74):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='57', width=199.75):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.86, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.05, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=91.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.47, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.96, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='59', width=187.61):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.1, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.2, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.3, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='60', width=188.55):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.13, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.13, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=99.13, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=142.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=15.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=12.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=57.32, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.64, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.64, default_y=30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=147.96, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=15.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=12.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=56.67, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=101.33, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.33, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=101.33, default_y=15.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=155.06, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=155.06, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.15, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=79.15, default_y=20.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=122.91, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=122.91, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=166.67, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.67, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=235.33, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=235.33, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=57.84, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=57.84, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=99.87, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=99.87, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=152.29, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=152.29, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='65', width=179.72):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=52.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.84, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=93.69, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=93.69, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=134.53, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='66', width=200.49):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=60.82, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.82, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=104.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=104.4, default_y=15.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=150.96, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.96, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='67', width=191.49):
            with Note(default_x=12.12, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=112.01, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.47, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.4, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.33, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.6, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.4, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.2, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.01, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.81, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.61, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.67, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.39, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=194.02, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.43, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.14, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='72', width=172.88):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=33.52, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.52, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=53.98, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.98, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=74.45, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=74.45, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=94.91, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=94.91, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.07, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.98, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=164.98, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=207.9, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.9, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=12.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.59, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=59.59, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=114.78, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.78, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=166.74, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.74, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.14, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.14, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=101.05, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=101.05, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=142.95, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.95, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.49, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='77', width=182.36):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.6, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.2, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.08, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.04, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='79', width=183.64):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.96, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.93, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.89, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=214.72):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='81', width=205.96):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.93, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.3, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='82', width=196.64):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.6, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.78, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=79.15, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=290.43, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=517.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=140.51):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=275.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=101.26, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.5, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.73, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=171.29):
            with Note(default_x=12.0, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=171.29):
            with Note(default_x=12.0, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.87, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=171.29):
            with Note(default_x=12.0, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-265.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=202.37):
            with Note(default_x=12.0, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.84, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.92, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=174.71, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=217.48, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=187.16):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.46, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.75, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=188.71):
            with Note(default_x=12.0, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.18, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.36, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=203.76):
            with Note(default_x=15.8, default_y=-260.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.37, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.27, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.37, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.51, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=162.99, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.18, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=224.69, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.99, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.97, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.96, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.89, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=147.81, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=198.9):
            with Note(default_x=12.0, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.58, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.76, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.34, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=189.58):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.56, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=143.73, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=80.09, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.66, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.33, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=109.2, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=153.07, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=149.83, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=196.24):
            with Note(default_x=12.36, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.51, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.19, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=79.15, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.86, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.56, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=207.27, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=186.24):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.41, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=186.24):
            with Note(default_x=12.0, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.71, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.41, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-160.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=217.32):
            with Note(default_x=12.0, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.86, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=164.79, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='25', width=208.56):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.73, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=113.5, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=160.23, default_y=-150.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=91.19, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=173.4, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=213.67, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=186.17):
            with Note(default_x=12.0, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.33, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.67, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=198.35):
            with Note(default_x=12.94, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=104.99, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.37, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.86, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.49, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=160.95, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.11, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.17, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.43, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.72, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=209.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.4, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=154.7, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=198.01):
            with Note(default_x=12.0, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.28, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.32, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.61, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=199.94):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.75, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.54, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=184.4):
            with Note(default_x=12.94, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.85, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.76, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.68, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.46, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.29, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=220.11, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.8, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.59, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=168.39, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.53, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.19, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=141.04, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=181.21):
            with Note(default_x=12.0, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.27, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.54, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=135.81, default_y=-265.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(230.9)
            with Note(default_x=79.15, default_y=-270.9, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=193.58, default_y=-250.9, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='42', width=182.74):
            with Note(default_x=12.0, default_y=-245.9, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.33, default_y=-255.9, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.88, default_y=-240.9, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.01, default_y=-275.9, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='43', width=173.42):
            with Note(default_x=17.23, default_y=-260.9, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.96, default_y=-245.9, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=130.76, default_y=-270.9, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='44', width=174.97):
            with Note(default_x=12.0, default_y=-255.9, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.6, default_y=-265.9, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.21, default_y=-260.9, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-245.9, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=29.82, default_y=-250.9, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=47.63, default_y=-255.9, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.45, default_y=-260.9, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='46', width=187.28):
            with Note(default_x=13.06, default_y=-265.9, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.43, default_y=-260.9, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=98.39, default_y=-255.9, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.53, default_y=-265.9, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.46, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.29, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.29, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.34, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.4, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.45, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.51, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.57, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.62, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=166.96):
            with Note(default_x=15.8, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.86, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.91, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.97, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.02, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.08, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.14, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.19, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=182.94):
            with Note(default_x=17.23, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.63, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.89, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.14, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.4, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.66, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.92, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.17, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=163.16):
            with Note(default_x=12.0, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.06, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.11, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.17, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.22, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.28, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.34, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.39, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=105.37):
            with Note(default_x=15.8, default_y=-260.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=140.06, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.3, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.86, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.41, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.88, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.67, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.55, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='56', width=200.74):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.21, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='57', width=199.75):
            with Note(default_x=12.0, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.86, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=109.19, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=153.05, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=91.19, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.47, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.96, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='59', width=187.61):
            with Note(default_x=12.0, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.1, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.2, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.3, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='60', width=188.55):
            with Note(default_x=12.94, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.13, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=142.23, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.32, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.64, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=147.96, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.67, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.33, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=155.06, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.91, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=166.67, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=235.33, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-260.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.84, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=99.87, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.29, default_y=-260.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='65', width=179.72):
            with Note(default_x=12.0, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.84, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=93.69, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=134.53, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='66', width=200.49):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.82, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=104.4, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.96, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='67', width=191.49):
            with Note(default_x=12.12, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=112.01, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.47, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.94, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.4, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.86, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.33, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.6, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.4, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.2, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.01, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.81, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.61, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.67, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.39, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=194.02, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.43, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.14, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='72', width=172.88):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=33.52, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.98, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.45, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.91, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=79.15, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.07, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.98, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=207.9, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.59, default_y=-250.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=114.78, default_y=-255.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.74, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.14, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.05, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.95, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-260.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.49, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='77', width=182.36):
            with Note(default_x=12.0, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.6, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.2, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.8, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=79.15, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.08, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.04, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='79', width=183.64):
            with Note(default_x=12.0, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.96, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.93, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.89, default_y=-160.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=214.72):
            with Note(default_x=12.0, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=162.84, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='81', width=205.96):
            with Note(default_x=12.0, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.93, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=112.3, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=158.23, default_y=-150.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='82', width=196.64):
            with Note(default_x=17.23, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.6, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=149.78, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=79.15, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=290.43, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=517.8, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=140.51):
            with Note(default_x=15.8, default_y=-155.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=275.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Attributes():
                Divisions(32.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note(default_x=101.26, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.5, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.73, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=171.29):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=171.29):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.87, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=171.29):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=50.44, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.87, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.31, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=202.37):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.9, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=263.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.92, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=174.71, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=217.48, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=187.16):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.46, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.75, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=188.71):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.18, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.36, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=203.76):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.37, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.27, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=208.49):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.37, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.51, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.99, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=274.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.18, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=224.69, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=191.12):
            with Note(default_x=12.0, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.99, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.97, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.96, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=197.35):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.89, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.81, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=198.9):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.58, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.76, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.34, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=189.58):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.56, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.73, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=263.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=80.09, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=122.66, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=199.77):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.33, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=109.2, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=153.07, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=195.88):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.83, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=195.88):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.26, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=196.24):
            with Note(default_x=12.36, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.51, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.19, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=253.39):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.86, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.56, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=207.27, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=186.24):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.41, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=186.24):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.71, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.41, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=140.12, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=217.32):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=164.79, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='25', width=208.56):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.73, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=113.5, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='26', width=258.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=91.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=173.4, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=213.67, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=186.17):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.33, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.67, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=198.35):
            with Note(default_x=12.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=104.99, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.37, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=205.95):
            with Note(default_x=17.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.86, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.49, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.95, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='30', width=202.7):
            with Note(default_x=12.0, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.11, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.17, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=265.16):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.43, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.72, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=209.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=204.23):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.7, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=198.01):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.28, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.32, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.61, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=199.94):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.75, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.54, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=184.4):
            with Note(default_x=12.94, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.85, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=96.76, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.68, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=266.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.46, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.29, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=220.11, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=221.56):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.8, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.59, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.39, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=195.76):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.53, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=107.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=186.44):
            with Note(default_x=17.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=141.04, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=181.21):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.27, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.54, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=135.81, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=243.11):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-270.9)
            with Note(default_x=79.15, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(48.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=193.58, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='42', width=182.74):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.33, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.88, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.01, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='43', width=173.42):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.96, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.76, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='44', width=174.97):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.6, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=90.21):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=29.82, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=47.63, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.45, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='46', width=187.28):
            with Note(default_x=13.06, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.43, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=98.39, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='47', width=264.94):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.46, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.29, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=168.39):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.29, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.34, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.4, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.45, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.51, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.57, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.62, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=166.96):
            with Note(default_x=15.8, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.86, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.91, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.97, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.02, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.08, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.14, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=182.94):
            with Note(default_x=17.23, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.63, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.89, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.14, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.4, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.66, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.92, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.17, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=163.16):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.06, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.11, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.17, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.22, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.28, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.34, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.39, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=105.37):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='53', width=164.95):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=140.06, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='54', width=292.57):
            with Note(default_x=14.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.3, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=203.86, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=234.41, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=193.75):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.88, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.67, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.55, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='56', width=200.74):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.55, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.21, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='57', width=199.75):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.86, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.19, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.05, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='58', width=278.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=91.19, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.47, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.96, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='59', width=187.61):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.1, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.2, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.3, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='60', width=188.55):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.13, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=142.23, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='61', width=195.38):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.32, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.64, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.96, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='62', width=202.16):
            with Note(default_x=12.0, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.67, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.33, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.06, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='63', width=281.97):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.91, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=166.67, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=235.33, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=198.07):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.84, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=99.87, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.29, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='65', width=179.72):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=93.69, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=134.53, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='66', width=200.49):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.82, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=104.4, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.96, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='67', width=191.49):
            with Note(default_x=12.12, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
        with Measure(number='68', width=239.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=112.01, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.47, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.94, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=173.4, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.86, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.33, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=193.18):
            with Note(default_x=15.8, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.6, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.4, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.2, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.01, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.81, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.61, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=253.34):
            with Note(default_x=15.8, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.67, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.39, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=194.02, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='71', width=193.26):
            with Note(default_x=12.0, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.43, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.14, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='72', width=172.88):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('16th')
            with Note(default_x=33.52, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.98, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.45, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.91, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=264.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note(default_x=79.15, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.07, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=164.98, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=207.9, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='74', width=215.93):
            with Note(default_x=12.0, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.59, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=114.78, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.74, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='75', width=188.67):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.14, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.05, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.95, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='76', width=200.71):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.49, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='77', width=182.36):
            with Note(default_x=12.0, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.6, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.2, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='78', width=250.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=163.08, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=205.04, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='79', width=183.64):
            with Note(default_x=12.0, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.96, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.93, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.89, default_y=-55.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=214.72):
            with Note(default_x=12.0, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.56, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.84, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='81', width=205.96):
            with Note(default_x=12.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.93, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.3, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='82', width=196.64):
            with Note(default_x=17.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.6, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.78, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='83', width=911.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note(default_x=79.15, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=290.43, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=517.8, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=140.51):
            with Note(default_x=15.8, default_y=-50.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(32.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')