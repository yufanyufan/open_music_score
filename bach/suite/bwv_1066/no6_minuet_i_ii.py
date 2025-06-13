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
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.98)
            PageWidth(1342.71)
            with PageMargins(type='even'):
                LeftMargin(63.9386)
                RightMargin(51.1509)
                TopMargin(63.9386)
                BottomMargin(44.757)
            with PageMargins(type='odd'):
                LeftMargin(51.1509)
                RightMargin(63.9386)
                TopMargin(31.9694)
                BottomMargin(38.3631)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Minuetto ', default_x=671.355, default_y=1867.01, justify='center', valign='top', font_size='24')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Oboe, Oboe 1')
            PartAbbreviation('Ob.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Oboe, Oboe 2')
            PartAbbreviation('Ob.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Fagotto, Fagott')
            PartAbbreviation('Fag.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Fagotto')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(71)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Violino, Violine 1')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Violino')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Violino, Violine 2')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Violino')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(7)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Viola, Viola')
            PartAbbreviation('Vla.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Viola')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(11)
                MidiProgram(42)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Violoncello, Basso Continuo')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(14)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=170.88):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(280.67)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-39.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Sound(tempo=96.0)
            with Note(default_x=85.57, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.42, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.52, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=96.71, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.38, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.04, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=72.98, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.04, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.35, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.67, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.99, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.3, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.84, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.78, default_y=20.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=50.25, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.89, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.52, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.16, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.02, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=126.39, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(49.7)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=60.71, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.22, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.22, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=101.43, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.1, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.4, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.25, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.98, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.24, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.5, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.76, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.02, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.2, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.05, default_y=20.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=51.89, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.55, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.22, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.88, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.2, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=131.1, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.0, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    TopSystemDistance(101.97)
            with Note(default_x=60.71, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.2, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=102.13, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=118.06, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.53, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=113.63, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.3, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=17.23, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.71, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=62.98, default_y=15.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.46, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.94, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.41, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.26, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.81, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=124.79, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.34, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.23, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.05, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=153.48):
            with Note(default_x=12.36, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.85, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.78, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.71, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=60.71, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.43, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=102.16, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=164.32, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.99, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.72, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.45, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=115.61, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.28, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.0, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.99, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.99, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.99, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.36, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.28, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=119.2, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.86, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(49.7)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=60.71, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.32, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.33, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=118.33, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=17.23, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.81, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.08, default_y=15.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.65, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.23, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.81, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.36, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.01, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=125.19, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.62, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.52, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.45, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=153.88):
            with Note(default_x=12.36, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.97, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.98, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.99, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=31.69, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.38, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=110.45, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.12, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(49.7)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=60.71, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.36, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=158.94, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.61, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.54, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.51, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.48, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.34, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.27, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.61, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='49', width=83.23):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='50', width=82.8):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='51', width=78.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='52', width=99.88):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='53', width=82.77):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='54', width=100.2):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='55', width=94.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    TopSystemDistance(101.97)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='57', width=86.09):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='58', width=85.66):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='59', width=81.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='60', width=102.74):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='61', width=85.62):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='62', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='63', width=97.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='64', width=59.98):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='65', width=82.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='66', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='67', width=86.69):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='68', width=98.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='70', width=117.48):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='71', width=86.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='72', width=98.94):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='73', width=101.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='74', width=107.51):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='75', width=103.63):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='76', width=100.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='77', width=82.03):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='78', width=92.71):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='79', width=85.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='80', width=60.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(49.7)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='82', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='83', width=82.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='84', width=94.68):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='85', width=90.13):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='86', width=113.04):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='87', width=81.75):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='88', width=94.5):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='89', width=96.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='90', width=103.07):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='91', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='92', width=95.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(49.7)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='94', width=100.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='95', width=93.36):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='96', width=68.08):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.79, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.86, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=106.97, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.64, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.17, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.08, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.09, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.46, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.83, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.19, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.56, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.97, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.88, default_y=20.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=53.82, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.69, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.55, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.42, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    TopSystemDistance(101.97)
            with Note(default_x=60.71, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.83, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=175.51, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.0, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.93, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=114.92, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.59, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=17.23, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.03, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.3, default_y=15.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.7, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.59, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.45, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=126.08, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.27, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.16, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.34, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(62.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=60.71, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.04, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.59, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=79.15, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-25.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-10.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-30.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-5.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.8, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.55, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.3, default_y=10.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.06, default_y=0.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=5.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-20.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-15.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=85.57, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.42, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.52, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=96.71, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.38, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.04, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=72.98, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.04, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.35, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.67, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.99, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.3, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.84, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.78, default_y=-85.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=50.25, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.89, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.52, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.16, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.02, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=126.39, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.22, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.22, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=101.43, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.1, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.4, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.25, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.98, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.24, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.5, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.76, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.02, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.2, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.05, default_y=-85.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=51.89, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.55, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.22, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.88, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.2, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=131.1, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.2, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=102.13, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=118.06, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.53, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=113.63, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.3, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=17.23, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.71, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=62.98, default_y=-90.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.46, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.94, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.41, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.26, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.81, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=124.79, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.34, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.23, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.05, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=153.48):
            with Note(default_x=12.36, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.85, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.78, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.71, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.43, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=102.16, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=164.32, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.99, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.72, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.45, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=115.61, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.28, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.0, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.99, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.99, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.99, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.28, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=119.2, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.86, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.32, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.33, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=118.33, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=17.23, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.81, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.08, default_y=-90.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.65, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.23, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.81, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.01, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=125.19, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.62, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.52, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.45, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=153.88):
            with Note(default_x=12.36, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.97, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.98, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.99, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=31.69, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.38, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=110.45, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.12, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=158.94, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.61, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.54, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.51, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.48, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.34, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.27, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.61, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='49', width=83.23):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='50', width=82.8):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='51', width=78.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='52', width=99.88):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='53', width=82.77):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='54', width=100.2):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='55', width=94.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='57', width=86.09):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='58', width=85.66):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='59', width=81.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='60', width=102.74):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='61', width=85.62):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='62', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='63', width=97.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='64', width=59.98):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='65', width=82.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='66', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='67', width=86.69):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='68', width=98.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='70', width=117.48):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='71', width=86.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='72', width=98.94):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='73', width=101.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='74', width=107.51):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='75', width=103.63):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='76', width=100.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='77', width=82.03):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='78', width=92.71):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='79', width=85.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='80', width=60.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='82', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='83', width=82.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='84', width=94.68):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='85', width=90.13):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='86', width=113.04):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='87', width=81.75):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='88', width=94.5):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='89', width=96.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='90', width=103.07):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='91', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='92', width=95.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='94', width=100.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='95', width=93.36):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='96', width=68.08):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.79, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.86, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=106.97, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.64, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.17, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.08, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.09, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.46, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.83, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.19, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.56, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.97, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.88, default_y=-85.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=53.82, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.69, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.55, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.42, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.83, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=175.51, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.93, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=114.92, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.59, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=17.23, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.03, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.3, default_y=-90.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.7, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.59, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.45, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=126.08, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.27, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.16, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.34, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.04, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.59, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=79.15, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-130.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-115.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-135.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-110.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.8, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.55, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.3, default_y=-95.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.06, default_y=-105.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-100.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-125.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-120.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=85.57, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.52, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.72, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.22, default_y=-195.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.98, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.35, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.99, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.78, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.25, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.89, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.52, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.02, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=105.26, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.07, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.33, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.59, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.85, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.11, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.37, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=73.22, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.29, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=81.86, default_y=-195.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.25, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.24, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.76, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.05, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.89, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.55, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.22, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.2, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=108.8, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.36, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=35.83, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.31, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.2, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.06, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.53, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.56, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.6, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.49, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=17.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.98, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.46, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.94, default_y=-190.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.35, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.81, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.35, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=104.25, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=153.48):
            with Note(default_x=12.72, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.55, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.42, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.69, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.85, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.71, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.43, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.16, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.88, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.6, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.45, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.17, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.89, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.61, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.0, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.99, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.99, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.72, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.97, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.23, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=73.48, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=93.73, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.99, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=49.28, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.58, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.89, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.32, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.33, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=17.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.08, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.65, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.23, default_y=-190.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.62, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.01, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.65, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=104.55, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.52, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='40', width=153.88):
            with Note(default_x=12.72, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.7, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.68, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.96, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.97, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.99, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.69, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.38, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.07, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.76, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.65, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.3, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.94, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.54, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.48, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.34, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.27, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='49', width=83.23):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='50', width=82.8):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='51', width=78.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='52', width=99.88):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='53', width=82.77):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='54', width=100.2):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='55', width=94.97):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='57', width=86.09):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='58', width=85.66):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='59', width=81.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='60', width=102.74):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='61', width=85.62):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='62', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='63', width=97.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='64', width=59.98):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='65', width=82.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='66', width=103.06):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='67', width=86.69):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='68', width=98.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='70', width=117.48):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='71', width=86.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='72', width=98.94):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='73', width=101.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='74', width=107.51):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='75', width=103.63):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='76', width=100.37):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='77', width=82.03):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='78', width=92.71):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='79', width=85.83):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='80', width=60.55):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='82', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='83', width=82.82):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='84', width=94.68):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='85', width=90.13):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='86', width=113.04):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='87', width=81.75):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='88', width=94.5):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='89', width=96.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='90', width=103.07):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='91', width=99.19):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='92', width=95.93):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='94', width=100.24):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='95', width=93.36):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='96', width=68.08):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.86, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.29, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.13, default_y=-195.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.08, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.46, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.19, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-200.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.88, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.82, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.69, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.55, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.83, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=154.28, default_y=-265.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.36, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.31, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.93, default_y=-240.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.26, default_y=-250.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.59, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=17.23, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.3, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-190.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.24, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.45, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.22, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.16, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.07, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.79, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=119.5, default_y=-245.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=145.21, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.04, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.01, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.35, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-210.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.67, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.01, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.35, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.68, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.8, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.55, default_y=-230.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.3, default_y=-205.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-225.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-220.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-215.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-235.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=85.57, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.42, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.52, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=96.71, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.38, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.04, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=72.98, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.04, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.35, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.67, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.99, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.3, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.84, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.78, default_y=-295.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=50.25, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.89, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.52, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.16, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.02, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=126.39, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.22, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.22, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=101.43, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.1, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.4, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.25, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.98, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.24, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.5, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.76, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.02, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.2, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.05, default_y=-295.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=51.89, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.55, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.22, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.88, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.2, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=131.1, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.2, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=102.13, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=118.06, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.53, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=113.63, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.3, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=17.23, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.71, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=62.98, default_y=-300.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.46, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.94, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.41, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.42, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.35, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.26, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.81, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=124.79, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.34, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.23, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.05, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=153.48):
            with Note(default_x=12.36, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.85, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.78, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.71, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.43, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=102.16, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=164.32, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.99, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.72, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.45, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=115.61, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.28, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.0, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.99, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.99, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.99, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.36, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.2, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=73.2, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.28, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=119.2, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.86, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.32, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.33, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=118.33, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=17.23, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.81, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.08, default_y=-300.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.65, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.23, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.81, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.36, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.01, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=125.19, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.62, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=88.52, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.45, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=153.88):
            with Note(default_x=12.36, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.97, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.98, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.99, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=31.69, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.38, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=110.45, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.12, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.62, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=69.62, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.36, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=158.94, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.61, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.54, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.51, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=69.48, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.34, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.27, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.61, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='49', width=83.23):
            with Note(default_x=15.8, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.13, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.47, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='50', width=82.8):
            with Note(default_x=16.2, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=37.12, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.04, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=78.97):
            with Note(default_x=12.36, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.28, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.2, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='52', width=99.88):
            with Note(default_x=15.44, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=70.79, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=82.77):
            with Note(default_x=16.16, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.08, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=100.2):
            with Note(default_x=17.23, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.97, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.86, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='55', width=94.97):
            with Note(default_x=12.0, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.74, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.63, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='57', width=86.09):
            with Note(default_x=15.8, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.56, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.33, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=85.66):
            with Note(default_x=16.2, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=38.55, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.9, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='59', width=81.82):
            with Note(default_x=12.36, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.06, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='60', width=102.74):
            with Note(default_x=15.44, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=72.69, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=85.62):
            with Note(default_x=16.16, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.51, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.86, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=103.06):
            with Note(default_x=17.23, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.4, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.29, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='63', width=97.83):
            with Note(default_x=12.0, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.17, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.06, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='64', width=59.98):
            with Note(default_x=12.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='65', width=82.24):
            with Note(default_x=12.36, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.92, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.47, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=103.06):
            with Note(default_x=17.23, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.29, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=86.69):
            with Note(default_x=17.23, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=39.58, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.93, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=98.55):
            with Note(default_x=12.36, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=69.78, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.51, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.23, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.96, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='70', width=117.48):
            with Note(default_x=12.72, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.11, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.5, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='71', width=86.19):
            with Note(default_x=16.16, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.79, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.43, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=98.94):
            with Note(default_x=15.44, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='73', width=101.37):
            with Note(default_x=16.16, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.53, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.4, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='74', width=107.51):
            with Note(default_x=20.0, default_y=-370.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=48.64, default_y=-375.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.28, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='75', width=103.63):
            with Note(default_x=17.23, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.13, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=74.58, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=100.37):
            with Note(default_x=17.23, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.41, default_y=-370.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.59, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='77', width=82.03):
            with Note(default_x=12.0, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.63, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.27, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=92.71):
            with Note(default_x=17.23, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=41.86, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.49, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='79', width=85.83):
            with Note(default_x=15.8, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.43, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.07, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=60.55):
            with Note(default_x=15.8, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.33, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.95, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='82', width=99.19):
            with Note(default_x=17.23, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.36, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='83', width=82.82):
            with Note(default_x=17.23, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=37.64, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.05, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='84', width=94.68):
            with Note(default_x=12.36, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=67.85, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=90.13):
            with Note(default_x=15.8, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.04, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.29, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='86', width=113.04):
            with Note(default_x=12.72, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.63, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.53, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='87', width=81.75):
            with Note(default_x=16.16, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.57, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.98, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='88', width=94.5):
            with Note(default_x=15.44, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='89', width=96.93):
            with Note(default_x=16.16, default_y=-355.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.31, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.18, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='90', width=103.07):
            with Note(default_x=20.0, default_y=-370.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=47.16, default_y=-375.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=74.31, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='91', width=99.19):
            with Note(default_x=17.23, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.13, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.36, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='92', width=95.93):
            with Note(default_x=17.23, default_y=-365.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.93, default_y=-370.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.63, default_y=-360.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.03, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.35, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='94', width=100.24):
            with Note(default_x=17.23, default_y=-350.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=44.37, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.5, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='95', width=93.36):
            with Note(default_x=15.8, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.12, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.44, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='96', width=68.08):
            with Note(default_x=15.8, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.79, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.86, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=106.97, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.64, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.17, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.08, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.09, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.46, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.83, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.19, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.56, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.97, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.88, default_y=-295.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=53.82, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.69, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.55, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.42, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.83, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=175.51, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.93, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=114.92, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.59, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=17.23, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.03, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.3, default_y=-300.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.7, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.06, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=70.24, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.59, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.45, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=126.08, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.27, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=89.16, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.34, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.04, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.59, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=79.15, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-340.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.68, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.35, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-325.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.23, default_y=-345.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=78.78, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-320.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.8, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.55, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.3, default_y=-305.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.06, default_y=-315.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-310.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-335.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-330.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=85.57, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.32, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=143.52, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.22, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.98, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.35, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.99, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=105.48):
            with Note(default_x=15.44, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=76.78, default_y=-425.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.25, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=91.52, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.12, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.02, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=126.39, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.21, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.22, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.86, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.25, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.24, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.76, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=110.2):
            with Note(default_x=15.44, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=80.05, default_y=-425.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.89, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.22, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=34.3, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=64.2, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=131.1, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.2, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=118.06, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.53, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=113.63, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.3, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=16.87, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=107.94, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.49, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.81, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.35, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=104.25, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.34, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.23, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=106.05, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=153.48):
            with Note(default_x=12.72, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=62.42, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=87.69, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.05, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=128.71, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='25', width=96.8):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=69.71, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.79, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.09, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.99, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.92, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.36, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=73.2, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.28, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=119.2, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.86, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.32, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.33, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=16.87, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.23, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.61, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.01, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.65, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=104.55, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.62, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.52, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=106.45, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='40', width=153.88):
            with Note(default_x=12.72, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=62.68, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=87.96, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.44, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=129.11, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='41', width=97.2):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=69.99, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.02, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.61, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.64, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.54, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.48, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.34, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.27, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.84, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='49', width=83.23):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.13, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.47, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='50', width=82.8):
            with Note(default_x=16.2, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.12, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.04, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='51', width=78.97):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=54.2, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='52', width=99.88):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.29, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.79, default_y=-485.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=82.77):
            with Note(default_x=16.16, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.08, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=100.2):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=42.97, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.86, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='55', width=94.97):
            with Note(default_x=12.0, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.74, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.63, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='57', width=86.09):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.56, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.33, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=85.66):
            with Note(default_x=16.2, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.55, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.9, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=81.82):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=57.06, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='60', width=102.74):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.25, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.69, default_y=-485.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=85.62):
            with Note(default_x=16.16, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.51, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.86, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=103.06):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=44.4, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=74.29, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='63', width=97.83):
            with Note(default_x=12.0, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.17, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.06, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=59.98):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='65', width=82.24):
            with Note(default_x=12.36, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.92, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.47, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=103.06):
            with Note(default_x=17.23, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=74.29, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=86.69):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.58, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.93, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='68', width=98.55):
            with Note(default_x=12.72, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.62, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=69.78, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.51, default_y=-480.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.23, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=113.96, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='70', width=117.48):
            with Note(default_x=12.72, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.11, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=81.5, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='71', width=86.19):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=61.43, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=98.94):
            with Note(default_x=15.8, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.98, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.16, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=101.37):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=72.4, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='74', width=107.51):
            with Note(default_x=20.0, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.64, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='75', width=103.63):
            with Note(default_x=16.87, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='76', width=100.37):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=44.41, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
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
        with Measure(number='77', width=82.03):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.63, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.27, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=92.71):
            with Note(default_x=17.23, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.86, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
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
        with Measure(number='79', width=85.83):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.43, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.07, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='80', width=60.55):
            with Note(default_x=15.8, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.33, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=101.95, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='82', width=99.19):
            with Note(default_x=17.23, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=72.36, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=82.82):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.64, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.05, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=94.68):
            with Note(default_x=12.72, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.62, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=67.85, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=90.13):
            with Note(default_x=15.8, default_y=-480.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.04, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.29, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='86', width=113.04):
            with Note(default_x=12.72, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.63, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=78.53, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='87', width=81.75):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=56.98, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='88', width=94.5):
            with Note(default_x=15.8, default_y=-475.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.5, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.2, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='89', width=96.93):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=70.18, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='90', width=103.07):
            with Note(default_x=20.0, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.16, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
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
        with Measure(number='91', width=99.19):
            with Note(default_x=16.87, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='92', width=95.93):
            with Note(default_x=17.23, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=42.93, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
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
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.03, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.35, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='94', width=100.24):
            with Note(default_x=17.23, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.37, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
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
        with Measure(number='95', width=93.36):
            with Note(default_x=15.8, default_y=-470.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.12, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.44, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='96', width=68.08):
            with Note(default_x=15.8, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.72, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.86, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.13, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.08, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.46, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.19, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='101', width=115.74):
            with Note(default_x=15.44, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=83.88, default_y=-425.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.82, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.55, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.94, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=111.83, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=175.51, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-465.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.24, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.93, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=114.92, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.59, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=16.87, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.9, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.45, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.22, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.27, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=89.16, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=107.34, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.07, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=119.5, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.21, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=175.02, default_y=-460.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=190.69, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='113', width=110.43):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=79.15, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-455.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.31, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.68, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.31, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.68, default_y=-440.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.8, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.3, default_y=-430.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-435.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-445.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.3, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-450.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note(default_x=85.57, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=143.52, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.22, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.98, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.36, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=89.99, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.78, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.25, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=91.52, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.12, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.02, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.14, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.26, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.22, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.86, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.25, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.36, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=93.76, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.05, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.89, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=95.22, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=34.3, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=64.2, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.5, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.8, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.2, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.06, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.53, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=91.6, default_y=-515.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=16.87, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=107.94, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.36, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=104.25, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=124.79, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.23, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=153.48):
            with Note(default_x=12.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.85, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.71, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.79, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.45, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.17, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.89, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=115.61, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.0, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.99, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.36, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.2, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.28, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=95.89, default_y=-515.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.32, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.33, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=16.87, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.23, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.36, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=104.55, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.19, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.52, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='40', width=153.88):
            with Note(default_x=12.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.97, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.99, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.02, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.0, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=119.65, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=139.3, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=158.94, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.54, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.48, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.34, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.27, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='49', width=83.23):
            with Note(default_x=15.8, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.77, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='50', width=82.8):
            with Note(default_x=16.2, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.12, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.04, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=78.97):
            with Note(default_x=12.36, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.28, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.2, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='52', width=99.88):
            with Note(default_x=15.8, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.29, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.79, default_y=-570.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=82.77):
            with Note(default_x=16.16, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.08, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=100.2):
            with Note(default_x=17.23, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.97, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.86, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='55', width=94.97):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.74, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.63, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='57', width=86.09):
            with Note(default_x=15.8, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.2, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='58', width=85.66):
            with Note(default_x=16.2, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.55, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.9, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='59', width=81.82):
            with Note(default_x=12.36, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.06, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='60', width=102.74):
            with Note(default_x=15.8, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.25, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.69, default_y=-570.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=85.62):
            with Note(default_x=16.16, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.51, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.86, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=103.06):
            with Note(default_x=17.23, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.4, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.29, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=97.83):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.17, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.06, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=59.98):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='65', width=82.24):
            with Note(default_x=12.36, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.56, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='66', width=103.06):
            with Note(default_x=17.23, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.13, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.29, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=86.69):
            with Note(default_x=17.23, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.58, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.93, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='68', width=98.55):
            with Note(default_x=12.72, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.62, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.78, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.15, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=113.96, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='70', width=117.48):
            with Note(default_x=12.72, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.11, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.5, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='71', width=86.19):
            with Note(default_x=16.16, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.79, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.43, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=98.94):
            with Note(default_x=15.44, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='73', width=101.37):
            with Note(default_x=16.16, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.53, default_y=-570.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.4, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='74', width=107.51):
            with Note(default_x=20.0, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.64, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='75', width=103.63):
            with Note(default_x=17.23, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-565.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=74.58, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='76', width=100.37):
            with Note(default_x=17.23, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.41, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=82.03):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=34.63, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.27, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=92.71):
            with Note(default_x=17.23, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.86, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=85.83):
            with Note(default_x=15.8, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.43, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.07, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=60.55):
            with Note(default_x=15.8, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.97, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='82', width=99.19):
            with Note(default_x=17.23, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.13, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='83', width=82.82):
            with Note(default_x=17.23, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.64, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.05, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=94.68):
            with Note(default_x=12.72, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.62, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.85, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='85', width=90.13):
            with Note(default_x=15.44, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=64.29, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='86', width=113.04):
            with Note(default_x=12.72, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.63, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.53, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='87', width=81.75):
            with Note(default_x=16.16, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.57, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.98, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='88', width=94.5):
            with Note(default_x=15.44, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='89', width=96.93):
            with Note(default_x=16.16, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.31, default_y=-570.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.18, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='90', width=103.07):
            with Note(default_x=20.0, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.16, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='91', width=99.19):
            with Note(default_x=17.23, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-565.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=72.36, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='92', width=95.93):
            with Note(default_x=17.23, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.93, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.03, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.35, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='94', width=100.24):
            with Note(default_x=17.23, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.37, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='95', width=93.36):
            with Note(default_x=15.8, default_y=-560.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.12, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.44, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='96', width=68.08):
            with Note(default_x=15.8, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.86, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.13, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.08, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.36, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=98.19, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.88, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.82, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=99.55, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.94, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=111.83, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.06, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=154.28, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.93, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=92.59, default_y=-515.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=16.87, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.9, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.36, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=105.22, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.08, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-520.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.16, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.04, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.15, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.31, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.67, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.01, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.35, default_y=-545.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.68, default_y=-555.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-550.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.68, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-525.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.8, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.3, default_y=-530.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-540.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-535.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=170.88):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=85.57, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.32, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.52, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=137.14):
            with Note(default_x=15.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.23, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.72, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.22, default_y=-615.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=101.68):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.1, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.98, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=134.07):
            with Note(default_x=12.72, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.35, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.99, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=105.48):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.9, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.78, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=136.93):
            with Note(default_x=17.23, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.25, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.89, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.52, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=160.76):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=63.02, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=105.26, default_y=-685.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=187.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.07, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.33, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.59, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.85, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.11, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.37, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=102.03):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.21, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=73.22, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=141.86):
            with Note(default_x=15.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.71, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.29, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=81.86, default_y=-615.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=106.4):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.55, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.25, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=138.79):
            with Note(default_x=12.72, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.24, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=93.76, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=110.2):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.35, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.05, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=141.64):
            with Note(default_x=17.23, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.89, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.55, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=95.22, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=165.48):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.2, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=108.8, default_y=-685.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=84.38):
            with Note(default_x=12.36, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=35.83, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.31, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='17', width=145.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.2, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.06, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=154.07):
            with Note(default_x=17.23, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.53, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.56, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.6, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=96.44):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.49, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.35, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=155.18):
            with Note(default_x=17.23, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.98, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.46, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.94, default_y=-610.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=96.44):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.49, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.35, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=149.56):
            with Note(default_x=12.72, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.81, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.35, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=104.25, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='23', width=130.82):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.51, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.23, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=153.48):
            with Note(default_x=12.72, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.55, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.42, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.69, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=96.8):
            with Note(default_x=12.36, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.85, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.71, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='26', width=204.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.43, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=102.16, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=122.88, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.6, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='27', width=102.0):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='28', width=156.05):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.45, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.17, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.89, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.61, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=102.0):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='30', width=128.76):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.0, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.99, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.99, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='31', width=83.98):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.46, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.92, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=138.75):
            with Note(default_x=12.72, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.97, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.23, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=73.48, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=93.73, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.99, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=102.0):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.2, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.2, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=159.63):
            with Note(default_x=17.23, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=49.28, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.58, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.89, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='35', width=145.55):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.32, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.33, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=155.58):
            with Note(default_x=17.23, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.08, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.65, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.23, default_y=-610.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=96.84):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.62, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=149.95):
            with Note(default_x=12.72, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.01, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.65, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=104.55, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='39', width=131.22):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.69, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.52, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='40', width=153.88):
            with Note(default_x=12.72, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=40.7, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.68, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.96, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=97.2):
            with Note(default_x=12.36, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.97, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.99, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='42', width=150.88):
            with Note(default_x=12.0, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.69, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.38, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.07, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.76, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='43', width=96.84):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.61, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.62, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=199.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.65, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.3, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.94, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=96.62):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.54, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.48, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='46', width=123.38):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.34, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.27, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=78.6):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.92, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.84, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=57.12):
            with Note(default_x=12.36, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='49', width=83.23):
            with Note(default_x=15.44, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='50', width=82.8):
            with Note(default_x=16.2, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.12, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.04, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='51', width=78.97):
            with Note(default_x=12.36, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=33.28, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.2, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='52', width=99.88):
            with Note(default_x=15.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.29, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.79, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=82.77):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=58.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='54', width=100.2):
            with Note(default_x=17.23, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.97, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.86, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='55', width=94.97):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.74, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.63, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='56', width=104.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='57', width=86.09):
            with Note(default_x=15.44, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='58', width=85.66):
            with Note(default_x=16.2, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.55, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.9, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='59', width=81.82):
            with Note(default_x=12.36, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.06, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='60', width=102.74):
            with Note(default_x=15.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.25, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.69, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=85.62):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=60.86, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='62', width=103.06):
            with Note(default_x=17.23, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.4, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.29, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='63', width=97.83):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.17, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.06, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='64', width=59.98):
            with Note(default_x=12.0, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='65', width=82.24):
            with Note(default_x=12.0, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='66', width=103.06):
            with Note(default_x=17.23, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.13, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=74.29, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=86.69):
            with Note(default_x=17.23, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.58, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.93, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=98.55):
            with Note(default_x=12.72, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.62, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.78, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=141.28):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.15, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=113.96, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='70', width=117.48):
            with Note(default_x=12.36, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=81.5, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='71', width=86.19):
            with Note(default_x=16.16, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.79, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.43, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='72', width=98.94):
            with Note(default_x=15.8, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.98, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.16, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=101.37):
            with Note(default_x=16.16, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.53, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.4, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=107.51):
            with Note(default_x=19.64, default_y=-675.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='75', width=103.63):
            with Note(default_x=17.23, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=74.58, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=100.37):
            with Note(default_x=16.87, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=82.03):
            with Note(default_x=12.0, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.63, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=57.27, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=92.71):
            with Note(default_x=17.23, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.86, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=85.83):
            with Note(default_x=15.8, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.43, default_y=-680.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.07, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='80', width=60.55):
            with Note(default_x=15.8, default_y=-690.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='81', width=126.71):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.35, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='82', width=99.19):
            with Note(default_x=17.23, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.13, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.36, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=82.82):
            with Note(default_x=17.23, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.64, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.05, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='84', width=94.68):
            with Note(default_x=12.72, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.62, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.85, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=90.13):
            with Note(default_x=15.44, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=64.29, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='86', width=113.04):
            with Note(default_x=12.36, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=78.53, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='87', width=81.75):
            with Note(default_x=16.16, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.57, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.98, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='88', width=94.5):
            with Note(default_x=15.8, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.5, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.2, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='89', width=96.93):
            with Note(default_x=16.16, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.31, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.18, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='90', width=103.07):
            with Note(default_x=19.64, default_y=-675.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='91', width=99.19):
            with Note(default_x=17.23, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.13, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=72.36, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='92', width=95.93):
            with Note(default_x=16.87, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='93', width=138.27):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.03, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.35, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='94', width=100.24):
            with Note(default_x=17.23, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.37, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='95', width=93.36):
            with Note(default_x=15.8, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.12, default_y=-680.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.44, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='96', width=68.08):
            with Note(default_x=15.8, default_y=-690.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='97', width=111.37):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.72, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.86, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='98', width=147.41):
            with Note(default_x=15.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.45, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.29, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.13, default_y=-615.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='99', width=111.94):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.26, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=80.08, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='100', width=144.33):
            with Note(default_x=12.72, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.46, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.19, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='101', width=115.74):
            with Note(default_x=15.8, default_y=-620.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.06, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.88, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=147.19):
            with Note(default_x=17.23, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=53.82, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.69, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=99.55, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='103', width=209.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=60.71, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.83, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=154.28, default_y=-685.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='104', width=80.07):
            with Note(default_x=12.36, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=33.83, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.31, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='105', width=97.73):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='106', width=155.36):
            with Note(default_x=17.23, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.93, default_y=-660.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.26, default_y=-670.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.59, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='107', width=97.73):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.89, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.24, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='108', width=156.47):
            with Note(default_x=17.23, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=63.3, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-610.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='109', width=97.73):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.89, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.24, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='110', width=150.85):
            with Note(default_x=12.72, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.45, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.22, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='111', width=132.11):
            with Note(default_x=12.0, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.09, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.16, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='112', width=215.45):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.07, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.79, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=119.5, default_y=-665.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=145.21, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='113', width=110.43):
            with Note(default_x=12.36, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.04, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.15, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='114', width=164.11):
            with Note(default_x=12.0, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.34, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.67, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.01, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.35, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='115', width=110.07):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-630.0, dynamics=111.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='116', width=164.11):
            with Note(default_x=12.0, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.67, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=79.01, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.35, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.68, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='117', width=110.07):
            with Note(default_x=12.0, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.68, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.78, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='118', width=136.82):
            with Note(default_x=12.0, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.8, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.55, default_y=-650.0, dynamics=111.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.3, default_y=-625.0, dynamics=111.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='119', width=92.05):
            with Note(default_x=12.0, default_y=-645.0, dynamics=111.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.15, default_y=-640.0, dynamics=111.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.3, default_y=-635.0, dynamics=111.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='120', width=74.81):
            with Note(default_x=12.36, default_y=-655.0, dynamics=111.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')