with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Fughetta: Vom Himmel hoch, da komm ich her')
    with Identification():
        Creator('J. S. Bach', type='composer')
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
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1223.92)
            PageWidth(1583.9)
            with PageMargins(type='even'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Fughetta: Vom Himmel hoch, da komm ich her', default_x=791.95, default_y=1167.23, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 701', default_x=791.95, default_y=1110.54, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1527.21, default_y=1028.23, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Organ')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Organ')
            with ScoreInstrument(id='P1-I2'):
                InstrumentName('Pan Flute')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
            MidiDevice(None, id='P1-I2', port=1)
            with MidiInstrument(id='P1-I2'):
                MidiChannel(2)
                MidiProgram(76)
                Volume(38.5827)
                Pan(-24.0)
        with ScorePart(id='P2'):
            PartName('Organ', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Organ')
            with ScoreInstrument(id='P2-I2'):
                InstrumentName('Pan Flute')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(3)
                MidiProgram(20)
                Volume(36.2205)
                Pan(0.0)
            MidiDevice(None, id='P2-I2', port=1)
            with MidiInstrument(id='P2-I2'):
                MidiChannel(4)
                MidiProgram(76)
                Volume(31.4961)
                Pan(27.0)
    with Part(id='P1'):
        with Measure(number='1', width=217.49):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(209.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                Instruments(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(1)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.67, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=82.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=141.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=178.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Instrument', default_y=6.2, font_weight='bold', font_size='12')
                Staff(2)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=399.68):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=51.7, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=76.45, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=101.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=125.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=150.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=175.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=200.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=224.89, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=249.63, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=274.37, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=299.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=323.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=348.6, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=373.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=101.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=200.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=299.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=420.72):
            with Note(default_x=12.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=104.79, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=160.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=212.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=53.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=79.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=104.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=134.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=160.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=186.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=212.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=237.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=263.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=290.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=316.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=341.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=367.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=393.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=211.66, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=411.63):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=237.56, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=262.2, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=286.84, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=311.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=336.12, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=360.75, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=385.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=40.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=65.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=89.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=114.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=139.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=163.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=188.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=212.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=114.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.92, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=311.48, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=459.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(147.43)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=59.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=360.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=83.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=113.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=137.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=162.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.21, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.34, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.47, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=258.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=282.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=162.07, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=258.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=360.91, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=385.04, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=409.18, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=433.31, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=497.54):
            with Note(default_x=15.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=257.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=28.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=51.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=81.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=110.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=140.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=269.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=290.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=319.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=349.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=378.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=140.24, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.56, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=198.89, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=228.21, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=257.54, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=319.98, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=378.64, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=407.96, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=437.29, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=466.61, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=492.94):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=250.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=74.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=104.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=133.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=263.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=286.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=315.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=344.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=374.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=133.37, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=162.66, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=191.96, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=221.25, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=251.15, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=315.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=374.16, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=403.45, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=432.75, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=462.04, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=553.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(147.43)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=71.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
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
            with Note(default_x=316.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=83.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=140.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=169.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=199.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=228.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=258.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=287.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=316.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=346.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=376.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=405.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=434.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=464.18, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=493.55, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=522.92, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=71.81, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=140.58, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=198.96, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=434.81, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=440.04):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=118.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=225.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=331.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=65.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=171.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=278.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=305.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=331.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=358.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=385.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=411.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.65, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.3, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.61, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=145.26, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.91, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=198.58, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=225.23, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=251.88, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=278.53, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=305.18, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=331.83, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.48, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.79, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=455.59):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=234.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=289.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=344.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=399.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=70.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=125.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=234.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=399.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=43.19, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=70.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=97.96, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=125.35, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=152.73, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=180.12, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=207.51, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=234.89, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=262.28, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=289.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=317.05, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=344.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=371.83, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=399.21, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=426.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=467.31):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=59.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=110.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=135.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=161.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=212.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=262.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=288.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=313.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=338.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=364.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=389.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=414.97, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=440.34, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=110.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=161.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=212.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=262.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=313.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=364.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=85.14, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=110.51, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=135.89, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=161.26, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=186.63, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=212.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=237.37, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=262.74, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=414.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=461.6):
            with Note(default_x=12.7, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=236.53, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=348.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(7)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=40.99, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.92, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.86, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.79, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.73, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.66, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.6, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.53, default_y=50.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=292.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=360.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=404.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=13.06, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=264.46, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=292.4, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=320.33, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=348.27, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=376.2, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=404.14, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=432.07, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=520.61):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=140.35, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=264.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=389.46, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=78.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=109.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=140.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=202.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=264.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=327.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=389.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=46.94, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=78.08, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.21, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=140.35, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.49, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=202.63, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=233.77, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=264.91, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=296.04, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=327.18, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=358.32, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=389.46, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=420.6, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=451.73, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=482.87, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=455.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(91.28)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(1)
            with Note(default_x=62.0, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=307.23, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=357.82, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=405.67, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=157.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=259.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=357.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=85.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=109.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=133.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=157.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=181.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=211.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=235.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=259.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=283.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=307.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=333.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=357.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=381.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=405.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=429.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=344.56):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=79.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=102.36, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=148.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=207.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
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
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=102.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=207.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=271.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=303.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=35.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=55.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=79.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=102.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=125.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=148.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=184.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=207.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=264.98):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=40.37, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=110.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=174.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=230.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=40.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=58.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=75.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=93.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=110.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=145.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=230.61, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.86, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=202.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=384.86):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=154.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=210.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=265.85, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=304.99, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=344.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=56.37, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=105.28, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=129.74, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=154.2, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=178.66, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=210.72, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=235.18, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=265.85, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=344.12, default_y=30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=105.28, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=210.72, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=265.85, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=304.99, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=344.12, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=456.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(91.28)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=59.77, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.4, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.91, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.38, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.9, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=202.41, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=261.23, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=407.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.37, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=155.38, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=178.9, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=202.41, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=225.93, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=261.23, default_y=30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.93, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=384.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=407.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=97.4, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.91, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.38, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=261.23, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=308.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=360.83, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=407.86, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
        with Measure(number='19', width=387.54):
            with Note(default_x=16.2, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.82, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.52, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=155.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.59, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=249.76, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=292.93, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=336.1, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=56.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=80.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=109.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(3.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=176.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=206.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=249.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=292.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.52, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=336.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=362.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=56.37, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=80.96, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.82, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.52, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.11, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.59, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.18, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=249.76, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=271.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=292.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=336.1, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=354.59):
            with Note(default_x=14.0, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=99.43, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=179.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=229.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=249.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=269.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=309.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=39.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=59.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=79.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=99.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=119.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=139.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=159.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=179.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=209.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=229.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=249.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=269.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=289.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=309.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=329.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.64, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=179.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=269.67, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=250.91):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=90.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=117.6, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=143.92, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=176.81, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=209.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=226.14, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=38.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=64.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=90.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=117.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=160.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=176.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=193.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=209.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.63, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.6, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=519.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(91.28)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=62.51, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=90.89, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=119.27, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=176.04, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=232.8, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=289.57, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=346.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=403.1, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=459.86, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=119.27, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=232.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=289.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=346.33, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=459.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.51, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=90.89, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.27, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=147.66, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=176.04, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.42, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=232.8, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=261.19, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=289.57, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=317.95, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=346.33, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=374.72, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=403.1, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=431.48, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=459.86, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=489.76, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=498.79):
            with Note(default_x=12.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.23, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=194.51, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.64, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.78, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=376.91, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=437.05, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=134.37, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=194.51, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=254.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=314.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=437.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=44.16, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=74.23, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=104.3, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=134.37, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=164.44, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=194.51, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=224.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=254.64, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=284.71, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=314.78, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=346.84, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=376.91, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=406.98, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=437.05, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=467.12, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=430.99):
            with Note(default_x=12.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=64.1, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.91, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=273.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=325.2, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=377.3, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=23.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=116.81, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=325.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=38.05, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=64.1, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=90.76, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=116.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=142.86, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=168.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=194.96, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=221.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=247.05, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=273.1, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=299.15, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=325.2, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=351.25, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=377.3, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=403.35, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=644.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=59.77, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=132.88, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=169.44, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=205.99, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=242.55, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=291.97, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=350.46, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=496.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=533.23, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=569.78, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=606.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=205.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=350.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=496.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=96.33, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=132.88, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=169.44, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=205.99, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=291.97, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=350.46, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=387.01, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=423.57, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=460.12, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=496.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=533.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=569.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=606.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=529.73):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=75.12, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=108.03, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=272.59, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=305.5, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
                        BreathMark(None)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.08, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Staff(1)
                Sound(tempo=70.0)
            with Note(default_x=370.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=1.0, relative_y=69.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=422.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(default_x=475.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=173.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=305.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=370.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=422.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=475.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=75.12, default_y=65.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=108.03, default_y=60.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=140.94, default_y=55.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.85, default_y=50.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=206.76, default_y=45.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=239.68, default_y=40.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=272.59, default_y=35.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=305.5, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=370.16, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=422.82, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=475.48, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
        with Measure(number='27', width=275.29):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.03, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(16.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=4.6, relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(16.0)
                Instrument(id='P1-I2')
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P1-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=217.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                Instruments(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=82.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=141.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=178.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=399.68):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=51.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.89, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.63, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.37, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=323.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=101.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=200.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=299.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=420.72):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=104.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.24, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=316.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=341.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=393.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(default_x=211.66, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=411.63):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=237.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=311.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=336.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.92, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=114.36, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.92, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=311.48, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=459.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=59.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=258.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=360.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=83.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.21, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.34, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.47, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=258.61, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=282.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=162.07, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=258.61, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=360.91, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=385.04, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=409.18, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.31, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=497.54):
            with Note(default_x=15.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=257.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=28.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=269.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=297.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=378.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=140.24, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.56, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.89, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.21, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=257.54, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=319.98, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=378.64, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=407.96, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=437.29, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=466.61, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=492.94):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=250.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=263.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=291.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=374.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=133.37, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=162.66, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.96, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.25, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=251.15, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=315.56, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=374.16, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=403.45, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=432.75, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.04, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=553.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=71.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
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
            with Note(default_x=316.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=83.68, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=111.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.95, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=316.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=346.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=434.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=464.18, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=493.55, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=522.92, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=71.81, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.58, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=198.96, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=434.81, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=440.04):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=118.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=225.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=331.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=65.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=171.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=225.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=278.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=331.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.65, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.3, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.95, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.61, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.26, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.91, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.58, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.23, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=251.88, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.53, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.18, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=331.83, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=358.48, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.14, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.79, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=455.59):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=234.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=289.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=344.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=399.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=70.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=234.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=399.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.19, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.57, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.96, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.35, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.73, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.12, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.51, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.89, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.28, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.67, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.05, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=344.44, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=371.83, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.21, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.6, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=467.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=59.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=212.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=262.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=364.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=389.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=414.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=440.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=161.26, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=212.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=262.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=313.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=364.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.14, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.51, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.89, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.26, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.63, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.0, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.37, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=262.74, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=414.97, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=461.6):
            with Note(default_x=12.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=236.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=348.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(6)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=40.99, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.92, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.86, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.79, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.73, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.66, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.6, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.53, default_y=-90.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=292.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=360.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=404.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=13.06, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=264.46, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=292.4, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.33, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=348.27, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=376.2, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=404.14, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=432.07, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=520.61):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=140.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=264.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=389.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=78.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=264.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=327.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=389.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.94, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.08, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.21, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.35, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.49, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.63, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.77, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=264.91, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.04, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.18, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.32, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=389.46, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=420.6, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=451.73, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=482.87, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=455.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=62.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=307.23, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=357.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=405.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=157.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=259.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=357.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.93, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.85, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.78, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=157.7, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.63, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.53, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.45, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=259.38, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.3, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.23, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.89, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=357.82, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=381.74, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.67, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=429.6, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=344.56):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=55.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=207.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
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
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=102.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=207.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=271.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=303.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.82, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.83, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.1, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.36, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.63, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.89, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.2, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.46, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=264.98):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=40.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=110.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=174.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=202.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=230.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=75.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=110.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=230.61, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.12, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.68, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.86, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=202.36, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=384.86):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=154.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=210.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=265.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=304.99, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=344.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.37, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=105.28, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.74, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.2, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.66, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=210.72, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.18, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=265.85, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=344.12, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=105.28, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=210.72, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=265.85, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=304.99, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=344.12, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='18', width=456.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=59.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=202.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=261.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=407.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=155.38, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=178.9, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.41, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.93, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=261.23, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=360.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=384.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=407.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=97.4, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.91, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.38, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=261.23, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=308.45, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=360.83, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=407.86, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
        with Measure(number='19', width=387.54):
            with Note(default_x=16.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.52, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=155.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=249.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=292.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=336.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=206.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=249.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=292.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.37, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.96, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.82, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.52, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=155.11, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.59, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.18, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.76, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.35, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=292.93, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=336.1, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='20', width=354.59):
            with Note(default_x=14.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=99.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=139.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=179.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=229.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=269.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=309.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=179.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=269.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=289.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.64, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=179.63, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=269.67, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=250.91):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=90.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=143.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=176.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=209.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=38.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=64.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=90.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=117.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=209.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.63, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=117.6, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.81, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=519.74):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=62.51, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=119.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=176.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=289.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=346.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=403.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=459.86, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=119.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=232.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=289.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=346.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=459.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.51, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.89, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.27, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.66, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.04, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.42, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.8, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.19, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=289.57, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=317.95, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.33, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.72, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=403.1, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=431.48, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=459.86, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=489.76, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=498.79):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=194.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=254.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=314.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=376.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=437.05, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=134.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=194.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=254.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=314.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=437.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.16, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.23, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.3, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.37, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.44, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.51, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.57, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=254.64, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.71, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.78, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.84, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=376.91, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=406.98, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=437.05, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=467.12, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=430.99):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=64.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=273.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=325.2, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=377.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=23.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=325.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.05, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.1, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.76, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.81, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.86, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.91, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.96, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.01, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.05, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.1, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.15, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=325.2, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=351.25, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.3, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.35, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=644.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(80.0)
            with Note(default_x=59.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=132.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.44, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=205.99, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.55, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=291.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=350.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=496.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=533.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=569.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=606.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=205.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=350.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=496.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=96.33, default_y=-95.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.88, default_y=-100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.44, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=205.99, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=291.97, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=350.46, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=387.01, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=423.57, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=460.12, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=496.68, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=533.23, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=569.78, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=606.34, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=529.73):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=75.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.03, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=272.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=305.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
                        BreathMark(None)
            with Note(default_x=365.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=422.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=475.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=173.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=305.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=365.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=422.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=475.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=75.12, default_y=-110.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.03, default_y=-115.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.94, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.85, default_y=-125.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.76, default_y=-130.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.68, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.59, default_y=-140.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=305.5, default_y=-145.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=365.16, default_y=-155.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=422.82, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=475.48, default_y=-160.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
        with Measure(number='27', width=275.29):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P2-I2')
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-180.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Instrument(id='P2-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-59.42, relative_y=-10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')