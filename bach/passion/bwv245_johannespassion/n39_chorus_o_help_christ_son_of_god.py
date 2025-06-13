with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 245')
        WorkTitle('Saint John Passion')
    MovementNumber('BWV 245 NBA #37')
    MovementTitle('O hilf, Christe, Gottes Sohn')
    with Identification():
        Creator('Edward J. Maurath', type='arranger')
        Creator('Johann Sebastian Bach (1685--1750)', type='composer')
        Creator('Baroque Passion Oratorio', type='poet')
        Rights('Sequenced by Edward J. Mauratth')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.2)
            Tenths(40.0)
        with PageLayout():
            PageHeight(3300.0)
            PageWidth(2333.33)
            with PageMargins(type='both'):
                LeftMargin(55.5555)
                RightMargin(55.5555)
                TopMargin(55.5555)
                BottomMargin(111.111)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('BWV 245=NBA #39 CORO=O hilf, Christe, Gottes Sohn', default_x=1166.67, default_y=3244.45, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('\n', default_x=1166.67, default_y=3188.89, justify='center', valign='top', font_size='14')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('Chorale in c minor from BWV 245 Saint John Passion\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('More Bach MuseScore files may be found at http://bach.ejmaurath.com\n')
        CreditWords('I uploaded this from Musescore 2')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)', default_x=2277.78, default_y=2551.56, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Mauratth', default_x=1166.67, default_y=111.111, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Flauto\nTraverso')
            PartAbbreviation('FLU')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Oboe')
            PartAbbreviation('OBO')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Violin\n1')
            PartAbbreviation('VN1')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Violin\n2')
            PartAbbreviation('VN2')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Viola\n1')
            PartAbbreviation('VLA')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P6'):
            PartName('Soprani')
            PartAbbreviation('SOP')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Boy Soprano')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Alti')
            PartAbbreviation('ALT')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(7)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Tenori')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(8)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Bassi')
            PartAbbreviation('BAS')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(9)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P10'):
            PartName('Bassoon\nContinuo')
            PartAbbreviation('BSN\nB.C.')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P10-I1', port=1)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(11)
                MidiProgram(71)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P11'):
            PartName('Bassono\nGrosso\nContinuo')
            PartAbbreviation('BSN\nB.C.')
            with ScoreInstrument(id='P11-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P11-I1', port=1)
            with MidiInstrument(id='P11-I1'):
                MidiChannel(12)
                MidiProgram(71)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P12'):
            PartName('Violoncelli\nContinuo')
            PartAbbreviation('VCI\nB.C.')
            with ScoreInstrument(id='P12-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P12-I1', port=1)
            with MidiInstrument(id='P12-I1'):
                MidiChannel(13)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P13'):
            PartName('Contrabassi\nContinuo')
            PartAbbreviation('CBI\nB.C.')
            with ScoreInstrument(id='P13-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P13-I1', port=1)
            with MidiInstrument(id='P13-I1'):
                MidiChannel(14)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P14'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P14-I1'):
                InstrumentName('Organ')
            MidiDevice(None, id='P14-I1', port=1)
            with MidiInstrument(id='P14-I1'):
                MidiChannel(15)
                MidiProgram(81)
                Volume(77.9528)
                Pan(0.0)
        with ScorePart(id='P15'):
            PartName('Cembalo\nContinuo')
            PartAbbreviation('CEM')
            with ScoreInstrument(id='P15-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P15-I1', port=1)
            with MidiInstrument(id='P15-I1'):
                MidiChannel(16)
                MidiProgram(7)
                Volume(57.4803)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=362.94):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(121.54)
                        RightMargin(0.0)
                    TopSystemDistance(762.88)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('60', default_x=-44.8, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note(default_x=128.63, default_y=5.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=5.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=5.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=5.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=0.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=0.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=5.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=5.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=0.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=122.62, default_y=-10.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-15.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-10.0, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.33, default_y=-5.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-15.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-15.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-20.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-25.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-30.0, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-25.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-20.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.4, default_y=-15.0, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.2, default_y=-15.0, dynamics=43.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-20.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.84, default_y=-25.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-30.0, dynamics=42.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(65.09)
                        RightMargin(0.0)
                    SystemDistance(328.26)
            with Note(default_x=98.78, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.21, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=201.65, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-10.0, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-5.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-10.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.69, default_y=-15.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.96, default_y=-15.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-5.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=5.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=5.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=0.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-5.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-10.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-10.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-10.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-5.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-10.0, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-15.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-20.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-25.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-30.0, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-20.0, dynamics=52.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-15.0, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.57, default_y=-15.0, dynamics=46.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-20.0, dynamics=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-25.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.33, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-100.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-100.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-100.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-100.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-105.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-110.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-115.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-110.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-105.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-100.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=-100.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-105.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-110.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=122.62, default_y=-115.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-120.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-115.0, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.33, default_y=-110.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-120.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-120.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-125.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-130.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-135.0, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-130.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-125.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.4, default_y=-120.0, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.2, default_y=-120.0, dynamics=43.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-125.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.84, default_y=-130.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-135.0, dynamics=42.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-120.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.21, default_y=-125.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=201.65, default_y=-120.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-115.0, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-110.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-115.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.69, default_y=-120.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.96, default_y=-120.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-110.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-105.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-100.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=-100.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-105.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-110.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-115.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-115.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-120.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-115.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-110.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-115.0, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-120.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-120.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-125.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-130.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-135.0, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-130.0, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-125.0, dynamics=52.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-120.0, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.57, default_y=-120.0, dynamics=46.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-125.0, dynamics=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-130.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.33, default_y=-135.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-135.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-205.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-205.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-205.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-205.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-210.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-215.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-220.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-215.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-210.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-205.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=-205.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-210.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-215.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=122.62, default_y=-220.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-225.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-220.0, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.33, default_y=-215.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-225.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-225.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-230.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-235.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-240.0, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-235.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-230.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.4, default_y=-225.0, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.2, default_y=-225.0, dynamics=43.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-230.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.84, default_y=-235.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-240.0, dynamics=42.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-225.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.21, default_y=-230.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=201.65, default_y=-225.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-220.0, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-215.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-220.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.69, default_y=-225.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.96, default_y=-225.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-215.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-210.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-205.0, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=-205.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-210.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-215.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-220.0, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-220.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-225.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-220.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-215.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-220.0, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-225.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-225.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-230.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-235.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-240.0, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-235.0, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-230.0, dynamics=52.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-225.0, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.57, default_y=-225.0, dynamics=46.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-230.0, dynamics=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-235.0, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.33, default_y=-240.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-240.0, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-335.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=183.39, default_y=-335.0, dynamics=70.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-330.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-325.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-330.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-330.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-335.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-345.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-340.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.32, default_y=-335.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=-335.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-340.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.57, default_y=-345.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-345.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-345.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-345.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.33, default_y=-345.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.66, default_y=-340.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-345.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.19, default_y=-350.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-355.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-350.0, dynamics=53.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-350.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=137.4, default_y=-345.0, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=198.2, default_y=-345.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=15.84, default_y=-350.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=146.59, default_y=-355.0, dynamics=44.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-345.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-350.0, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.65, default_y=-345.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.08, default_y=-340.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-345.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.06, default_y=-345.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.96, default_y=-340.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-335.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-335.0, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-335.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=-330.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.36, default_y=-330.0, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=141.0, default_y=-335.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-345.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.31, default_y=-345.0, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.83, default_y=-345.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.22, default_y=-340.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-345.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.67, default_y=-350.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-355.0, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-350.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-345.0, dynamics=57.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.04, default_y=-340.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.57, default_y=-340.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-345.0, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.24, default_y=-350.0, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=200.77, default_y=-355.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-360.0, dynamics=50.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-465.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.39, default_y=-465.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.14, default_y=-460.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=292.9, default_y=-465.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=327.12, default_y=-460.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-455.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.08, default_y=-450.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=86.16, default_y=-445.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.95, default_y=-465.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-470.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-470.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.32, default_y=-465.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=196.58, default_y=-470.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=210.05):
            with Note(default_x=15.8, default_y=-470.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=122.62, default_y=-475.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-460.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-465.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.33, default_y=-470.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=173.99, default_y=-465.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=211.66, default_y=-460.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=249.32, default_y=-455.0, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-450.0, dynamics=57.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-470.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-470.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-470.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-470.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-465.0, dynamics=50.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=137.4, default_y=-460.0, dynamics=46.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=198.2, default_y=-460.0, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-465.0, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.52, default_y=-460.0, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.84, default_y=-455.0, dynamics=47.78):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-470.0, dynamics=42.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-460.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-465.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.65, default_y=-470.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.08, default_y=-470.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-470.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.43, default_y=-475.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.06, default_y=-460.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.96, default_y=-460.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-450.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.18, default_y=-465.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.36, default_y=-460.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.09, default_y=-460.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-455.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.88, default_y=-450.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=77.04, default_y=-445.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.0, default_y=-450.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-470.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.31, default_y=-475.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=126.83, default_y=-470.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-465.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.22, default_y=-460.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=230.92, default_y=-455.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-450.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-470.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-470.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-470.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-470.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-460.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.04, default_y=-460.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.57, default_y=-460.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-460.0, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.3, default_y=-465.0, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.61, default_y=-470.0, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.69, default_y=-475.0, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=200.77, default_y=-470.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-475.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-520.0, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-520.0, dynamics=70.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-520.0, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-520.0, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-525.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-530.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-535.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-530.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-525.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-520.0, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=-520.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-525.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-530.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=122.62, default_y=-535.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-540.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-535.0, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.33, default_y=-530.0, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-540.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-540.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-545.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-550.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-555.0, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-550.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-545.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.4, default_y=-540.0, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.2, default_y=-540.0, dynamics=43.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-545.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.84, default_y=-550.0, dynamics=50.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-555.0, dynamics=42.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.09)
            with Note(default_x=98.78, default_y=-541.09, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.21, default_y=-546.09, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=201.65, default_y=-541.09, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-536.09, dynamics=65.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-531.09, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-536.09, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.69, default_y=-541.09, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.96, default_y=-541.09, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-531.09, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-526.09, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-521.09, dynamics=78.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=-521.09, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-526.09, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-531.09, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-536.09, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-536.09, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-541.09, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-536.09, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-531.09, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-536.09, dynamics=62.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-541.09, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-541.09, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-546.09, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-551.09, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-556.09, dynamics=55.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-551.09, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-546.09, dynamics=52.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-541.09, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.57, default_y=-541.09, dynamics=46.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-546.09, dynamics=50.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-551.09, dynamics=53.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.33, default_y=-556.09, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-556.09, dynamics=44.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-650.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=183.39, default_y=-650.0, dynamics=70.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-645.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-640.0, dynamics=68.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-645.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-645.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-650.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-660.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-655.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.32, default_y=-650.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.58, default_y=-650.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-655.0, dynamics=73.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.57, default_y=-660.0, dynamics=76.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-660.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-660.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-660.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.33, default_y=-660.0, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.66, default_y=-655.0, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-660.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.19, default_y=-665.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-670.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-665.0, dynamics=53.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-665.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=137.4, default_y=-660.0, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=198.2, default_y=-660.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=15.84, default_y=-665.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=146.59, default_y=-670.0, dynamics=44.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-661.09, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-666.09, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.65, default_y=-661.09, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.08, default_y=-656.09, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-661.09, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.06, default_y=-661.09, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.96, default_y=-656.09, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-651.09, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-651.09, dynamics=74.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-651.09, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.09, default_y=-646.09, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.36, default_y=-646.09, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=141.0, default_y=-651.09, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-661.09, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.31, default_y=-661.09, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.83, default_y=-661.09, dynamics=65.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.22, default_y=-656.09, dynamics=58.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-661.09, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.67, default_y=-666.09, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-671.09, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-666.09, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-661.09, dynamics=57.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.04, default_y=-656.09, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.57, default_y=-656.09, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-661.09, dynamics=53.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.24, default_y=-666.09, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=200.77, default_y=-671.09, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-676.09, dynamics=50.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=128.63, default_y=-780.0, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.39, default_y=-780.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.14, default_y=-775.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=292.9, default_y=-780.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=327.12, default_y=-775.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-770.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.08, default_y=-765.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=86.16, default_y=-760.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=159.95, default_y=-780.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-785.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-785.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.32, default_y=-780.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=196.58, default_y=-785.0, dynamics=71.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=210.05):
            with Note(default_x=15.8, default_y=-785.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=122.62, default_y=-790.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-775.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-780.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.33, default_y=-785.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=173.99, default_y=-780.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=211.66, default_y=-775.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=249.32, default_y=-770.0, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-765.0, dynamics=57.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.09, default_y=-785.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.19, default_y=-785.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-785.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-785.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-780.0, dynamics=50.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=137.4, default_y=-775.0, dynamics=46.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=198.2, default_y=-775.0, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-780.0, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.52, default_y=-775.0, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.84, default_y=-770.0, dynamics=47.78):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.59, default_y=-785.0, dynamics=42.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.78, default_y=-776.09, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-781.09, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.65, default_y=-786.09, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.08, default_y=-786.09, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-786.09, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.43, default_y=-791.09, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.06, default_y=-776.09, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.96, default_y=-776.09, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-766.09, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.18, default_y=-781.09, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.36, default_y=-776.09, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.09, default_y=-776.09, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-771.09, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.88, default_y=-766.09, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=77.04, default_y=-761.09, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.0, default_y=-766.09, dynamics=62.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-786.09, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.31, default_y=-791.09, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=126.83, default_y=-786.09, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-781.09, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.22, default_y=-776.09, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=230.92, default_y=-771.09, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-766.09, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.84, default_y=-786.09, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.67, default_y=-786.09, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-786.09, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-786.09, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-776.09, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.04, default_y=-776.09, dynamics=56.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.57, default_y=-776.09, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-776.09, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.3, default_y=-781.09, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.61, default_y=-786.09, dynamics=54.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.69, default_y=-791.09, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=200.77, default_y=-786.09, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-791.09, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=128.63, default_y=-845.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-845.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-830.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-835.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-840.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-845.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.23, default_y=-850.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=159.95, default_y=-845.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-830.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-840.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-855.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=196.58, default_y=-855.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-850.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-865.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-845.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-830.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-835.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=136.33, default_y=-830.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-840.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-855.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=94.19, default_y=-850.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.97, default_y=-865.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-850.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.6, default_y=-865.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=137.4, default_y=-875.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-875.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-870.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.84, default_y=-870.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=146.59, default_y=-865.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.09)
            with Note(default_x=98.78, default_y=-867.19, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-862.19, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.65, default_y=-857.19, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-852.19, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-847.19, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-857.19, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.96, default_y=-842.19, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-847.19, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-837.19, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-822.19, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.23, default_y=-827.19, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.09, default_y=-832.19, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=221.95, default_y=-837.19, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-842.19, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-847.19, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-852.19, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-847.19, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-857.19, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-847.19, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-832.19, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-837.19, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-842.19, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-857.19, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=83.67, default_y=-852.19, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.05, default_y=-867.19, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-852.19, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.42, default_y=-857.19, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-877.19, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.31, default_y=-872.19, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=183.57, default_y=-867.19, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=215.83, default_y=-862.19, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-857.19, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-852.19, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.33, default_y=-847.19, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-847.19, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-880.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=128.63, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-5.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=10.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=0.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.23, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=159.95, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=10.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=196.58, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=10.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=5.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=136.33, default_y=10.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=94.19, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.97, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-10.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.6, default_y=-25.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=137.4, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-35.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-30.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.84, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=146.59, default_y=-25.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-882.19)
            with Note(default_x=98.78, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.65, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-10.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.96, default_y=0.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=20.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=154.23, default_y=15.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=188.09, default_y=10.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=221.95, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-5.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=109.2, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=141.0, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-15.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-5.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=10.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=161.53, default_y=5.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.22, default_y=0.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-15.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=83.67, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.05, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-10.0, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.42, default_y=-15.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=151.31, default_y=-30.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=183.57, default_y=-25.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=215.83, default_y=-20.0, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-15.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-10.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.33, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P11'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note(default_x=128.63, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-5.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=10.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=0.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.23, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=159.95, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=10.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=196.58, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=10.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=5.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=136.33, default_y=10.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=94.19, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.97, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-10.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.6, default_y=-25.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=137.4, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-35.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-30.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.84, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=146.59, default_y=-25.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=98.78, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.65, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-10.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.96, default_y=0.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=20.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=154.23, default_y=15.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=188.09, default_y=10.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=221.95, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-5.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=109.2, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=141.0, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-15.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-5.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=10.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=161.53, default_y=5.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.22, default_y=0.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-15.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=83.67, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.05, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-10.0, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.42, default_y=-15.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=151.31, default_y=-30.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=183.57, default_y=-25.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=215.83, default_y=-20.0, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-15.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-10.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.33, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P12'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(945.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=128.63, default_y=-950.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-950.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=-935.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-940.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-945.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-950.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.23, default_y=-955.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=159.95, default_y=-950.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-935.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-945.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-960.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=196.58, default_y=-960.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-955.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-970.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-950.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-935.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=-940.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=136.33, default_y=-935.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=-945.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-960.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=94.19, default_y=-955.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.97, default_y=-970.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-955.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.6, default_y=-970.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=137.4, default_y=-980.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-980.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-975.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.84, default_y=-975.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=146.59, default_y=-970.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(947.19)
            with Note(default_x=98.78, default_y=-972.19, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-967.19, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.65, default_y=-962.19, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-957.19, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-952.19, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-962.19, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.96, default_y=-947.19, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-952.19, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=-942.19, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=-927.19, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.23, default_y=-932.19, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.09, default_y=-937.19, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=221.95, default_y=-942.19, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-947.19, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-952.19, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.2, default_y=-957.19, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.0, default_y=-952.19, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-962.19, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-952.19, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=-937.19, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.53, default_y=-942.19, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-947.19, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-962.19, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=83.67, default_y=-957.19, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.05, default_y=-972.19, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-957.19, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.42, default_y=-962.19, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-982.19, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.31, default_y=-977.19, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=183.57, default_y=-972.19, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=215.83, default_y=-967.19, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-962.19, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-957.19, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.33, default_y=-952.19, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-952.19, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P13'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-985.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note(default_x=128.63, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=183.39, default_y=-5.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.14, default_y=10.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=0.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.23, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=159.95, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=10.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.32, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=196.58, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.57, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=10.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.06, default_y=5.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=136.33, default_y=10.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=211.66, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=94.19, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=157.97, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-10.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.6, default_y=-25.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=137.4, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-35.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-30.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.84, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=146.59, default_y=-25.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-987.19)
            with Note(default_x=98.78, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=201.65, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=253.08, default_y=-10.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.06, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=149.96, default_y=0.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=66.18, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=120.36, default_y=20.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=154.23, default_y=15.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=188.09, default_y=10.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=221.95, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.04, default_y=-5.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=109.2, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=141.0, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-15.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.31, default_y=-5.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.83, default_y=10.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=161.53, default_y=5.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=196.22, default_y=0.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-15.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=83.67, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.05, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-10.0, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.42, default_y=-15.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.04, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=151.31, default_y=-30.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=183.57, default_y=-25.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=215.83, default_y=-20.0, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-15.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.61, default_y=-10.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.33, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P14'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(1)
                    Chromatic(2.0)
            with Note(default_x=128.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=128.63, default_y=-25.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=183.39, default_y=-25.0, dynamics=70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.14, default_y=-20.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.9, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.16, default_y=-20.0, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.95, default_y=-25.0, dynamics=61.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-30.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=136.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.32, default_y=-25.0, dynamics=71.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.58, default_y=-25.0, dynamics=68.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=210.05):
            with Note(default_x=16.16, default_y=-30.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=69.57, default_y=-35.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=122.62, default_y=-35.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.06, default_y=-35.0, dynamics=64.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=136.33, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=211.66, default_y=-30.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.19, default_y=-40.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.97, default_y=-45.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-40.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.6, default_y=-40.0, dynamics=51.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=137.4, default_y=-40.0, dynamics=48.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.2, default_y=-40.0, dynamics=46.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=228.45):
            with Note(default_x=15.84, default_y=-40.0, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=146.59, default_y=-45.0, dynamics=44.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=98.78, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.21, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.65, default_y=-35.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=253.08, default_y=-30.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.06, default_y=-35.0, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=149.96, default_y=-30.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.18, default_y=-25.0, dynamics=74.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.36, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.09, default_y=-20.0, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=213.71):
            with Note(default_x=12.36, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=141.0, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.31, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.83, default_y=-35.0, dynamics=65.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=196.22, default_y=-30.0, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-35.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.67, default_y=-40.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.05, default_y=-45.0, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-40.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.42, default_y=-35.0, dynamics=57.78):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.04, default_y=-30.0, dynamics=54.44):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=183.57, default_y=-30.0, dynamics=51.11):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=12.0, default_y=-35.0, dynamics=53.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=48.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=84.24, default_y=-40.0, dynamics=55.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=200.77, default_y=-45.0, dynamics=57.78):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.77, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-50.0, dynamics=50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Note(default_x=15.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P15'):
        with Measure(number='1', width=362.94):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-3)
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
            with Note(default_x=128.63, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=128.63, default_y=-45.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.63, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.39, default_y=-45.0, dynamics=70.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.39, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=238.14, default_y=-40.0, dynamics=67.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=238.14, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=292.9, default_y=-45.0, dynamics=71.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=292.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=327.12, default_y=-40.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=128.63, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=183.39, default_y=-5.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=238.14, default_y=10.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=292.9, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=243.48):
            with Note(default_x=12.0, default_y=-35.0, dynamics=66.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=49.08, default_y=-30.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=86.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=159.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=159.95, default_y=-45.0, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.0, default_y=0.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=86.16, default_y=-5.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=123.23, default_y=-10.0, dynamics=76.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=159.95, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=258.44):
            with Note(default_x=15.8, default_y=-40.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.06, default_y=-50.0, dynamics=70.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.06, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.32, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.32, default_y=-55.0, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.32, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=196.58, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.58, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=208.44, default_y=-50.0, dynamics=71.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=10.0, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.06, default_y=0.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.32, default_y=-15.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=196.58, default_y=-15.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=210.05):
            with Note(default_x=15.8, default_y=-50.0, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=122.62, default_y=-55.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=122.62, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.16, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.57, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=122.62, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=288.59):
            with Note(default_x=15.8, default_y=-40.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.06, default_y=-45.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.33, default_y=-40.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.99, default_y=-45.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=211.66, default_y=-40.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=249.32, default_y=-35.0, dynamics=60.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=10.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.06, default_y=5.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=136.33, default_y=10.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=211.66, default_y=0.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=248.14):
            with Note(default_x=14.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-30.0, dynamics=57.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=54.09, default_y=-50.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.19, default_y=-50.0, dynamics=58.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.19, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=157.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=157.97, default_y=-50.0, dynamics=53.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=157.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=14.0, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=94.19, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.97, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=260.6):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0, dynamics=53.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=76.6, default_y=-45.0, dynamics=50.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=137.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=137.4, default_y=-40.0, dynamics=46.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=198.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=198.2, default_y=-40.0, dynamics=48.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.6, default_y=-25.0, dynamics=52.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=137.4, default_y=-35.0, dynamics=54.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=198.2, default_y=-35.0, dynamics=51.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=228.45):
            with Note(default_x=16.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-45.0, dynamics=52.22):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=52.52, default_y=-40.0, dynamics=50.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.84, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=88.84, default_y=-35.0, dynamics=47.78):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.59, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=146.59, default_y=-50.0, dynamics=42.22):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=146.59, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.2, default_y=-30.0, dynamics=47.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.84, default_y=-30.0, dynamics=44.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=146.59, default_y=-25.0, dynamics=38.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=306.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=98.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.78, default_y=-40.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=150.21, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=150.21, default_y=-45.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.65, default_y=-50.0, dynamics=65.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.65, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=253.08, default_y=-50.0, dynamics=62.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=98.78, default_y=-25.0, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=150.21, default_y=-20.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.65, default_y=-15.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=253.08, default_y=-10.0, dynamics=71.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=225.91):
            with Note(default_x=15.8, default_y=-50.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=49.43, default_y=-55.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=83.06, default_y=-40.0, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=149.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=149.96, default_y=-40.0, dynamics=53.33):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=149.96, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-5.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=83.06, default_y=-15.0, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.96, default_y=0.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=257.42):
            with Note(default_x=12.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.18, default_y=-45.0, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.18, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=120.36, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=120.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=188.09, default_y=-40.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=188.09, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=188.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.0, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.18, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.36, default_y=20.0, dynamics=62.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=154.23, default_y=15.0, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=188.09, default_y=10.0, dynamics=66.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=221.95, default_y=5.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=213.71):
            with Note(default_x=12.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=12.72, default_y=-35.0, dynamics=71.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=44.88, default_y=-30.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.04, default_y=-25.0, dynamics=66.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=141.0, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=141.0, default_y=-30.0, dynamics=62.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.72, default_y=0.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.04, default_y=-5.0, dynamics=73.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=109.2, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=141.0, default_y=-5.0, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=267.22):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.31, default_y=-55.0, dynamics=76.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=71.31, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=126.83, default_y=-40.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=126.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=161.53, default_y=-45.0, dynamics=70.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=196.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=196.22, default_y=-40.0, dynamics=66.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=230.92, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-15.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.31, default_y=-5.0, dynamics=61.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=126.83, default_y=10.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=161.53, default_y=5.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=196.22, default_y=0.0, dynamics=60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=217.65):
            with Note(default_x=14.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-30.0, dynamics=58.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.84, default_y=-50.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=83.67, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=83.67, default_y=-50.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=83.67, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=139.05, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=139.05, default_y=-50.0, dynamics=55.56):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=139.05, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=14.0, default_y=-15.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=83.67, default_y=-10.0, dynamics=61.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.05, default_y=-25.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=249.7):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.42, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.42, default_y=-40.0, dynamics=58.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.04, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.04, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.04, default_y=-40.0, dynamics=56.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.57, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.57, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.57, default_y=-40.0, dynamics=53.33):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=55.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.42, default_y=-15.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.04, default_y=-35.0, dynamics=62.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=151.31, default_y=-30.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=183.57, default_y=-25.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=215.83, default_y=-20.0, dynamics=55.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=260.46):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0, dynamics=50.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.3, default_y=-45.0, dynamics=52.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=84.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.61, default_y=-50.0, dynamics=54.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.61, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=142.69, default_y=-55.0, dynamics=56.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=142.69, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=200.77, default_y=-50.0, dynamics=53.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=200.77, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=200.77, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.0, default_y=-15.0, dynamics=53.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.61, default_y=-10.0, dynamics=51.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.33, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=158.95):
            with Note(default_x=15.6, default_y=-55.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(1)
            with Note(default_x=15.6, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.6, default_y=-5.0, dynamics=46.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')