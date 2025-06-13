with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 245')
        WorkTitle('Saint John Passion')
    MovementNumber('BWV 245 NBA #18')
    MovementTitle('Da sprach Pilatus zu ihm')
    with Identification():
        Creator('Edward J. Maurath', type='arranger')
        Creator('Johann Sebastian Bach', type='composer')
        Creator('Saint John', type='lyricist')
        Creator('Baroque Passion Oratorio', type='poet')
        Creator('Martin Luther', type='translator')
        Rights('Sequenced by Edward J. Maurath')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/272961/scores/5438336')
    with Defaults():
        with Scaling():
            Millimeters(8.0)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2970.0)
            PageWidth(2100.0)
            with PageMargins(type='both'):
                LeftMargin(50.0)
                RightMargin(50.0)
                TopMargin(50.0)
                BottomMargin(100.0)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('BWV 245 NBA #18 Da sprach Pilatus zu ihm', default_x=1050.0, default_y=2920.0, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('\n', default_x=1050.0, default_y=2870.0, justify='center', valign='top', font_size='14')
        CreditWords('Recitativo and Chorus from the Saint John Passion\n')
        CreditWords('More at http://bach.ejmaurath.com\n')
        CreditWords('I reccommend AGAINST loading this into Musescore 3')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)\n', default_x=2050.0, default_y=2686.16, justify='right', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Saint John, Heilige Schrift, Martin Luther\n', default_x=50.0, default_y=2686.16, justify='left', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=1050.0, default_y=100.0, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=1050.0, default_y=100.0, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Flauti\nTraversi')
            PartAbbreviation('FLU')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(57.4803)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Oboe\n1')
            PartAbbreviation('OB1')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(69)
                Volume(57.4803)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Oboe\n2')
            PartAbbreviation('OB2')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Oboe da caccia')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(69)
                Volume(59.8425)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Violin\n1')
            PartAbbreviation('VN1')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(41)
                Volume(49.6063)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Violin\n2')
            PartAbbreviation('VN2')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(41)
                Volume(48.8189)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Viola')
            PartAbbreviation('VLE')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(42)
                Volume(50.3937)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Evangelista')
            PartAbbreviation('EVA')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Soprano')
            with ScoreInstrument(id='P7-I2'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(7)
                MidiProgram(59)
                Volume(100.0)
                Pan(0.0)
            MidiDevice(None, id='P7-I2', port=1)
            with MidiInstrument(id='P7-I2'):
                MidiChannel(8)
                MidiProgram(42)
                Volume(62.2047)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P8'):
            PartName('Soprani')
            PartAbbreviation('SOP')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Boy Soprano')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(9)
                MidiProgram(53)
                Volume(59.8425)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Alti')
            PartAbbreviation('ALT')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(11)
                MidiProgram(53)
                Volume(60.6299)
                Pan(0.0)
        with ScorePart(id='P10'):
            PartName('Tenori')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P10-I1', port=1)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(12)
                MidiProgram(53)
                Volume(62.2047)
                Pan(0.0)
        with ScorePart(id='P11'):
            PartName('Bassi')
            PartAbbreviation('BAS')
            with ScoreInstrument(id='P11-I1'):
                InstrumentName('Bass')
            with ScoreInstrument(id='P11-I2'):
                InstrumentName('Bass')
            with ScoreInstrument(id='P11-I3'):
                InstrumentName('Bass')
            with ScoreInstrument(id='P11-I4'):
                InstrumentName('Bass')
            with ScoreInstrument(id='P11-I5'):
                InstrumentName('Bass')
            MidiDevice(None, id='P11-I1', port=1)
            with MidiInstrument(id='P11-I1'):
                MidiChannel(13)
                MidiProgram(81)
                Volume(100.0)
                Pan(0.0)
            MidiDevice(None, id='P11-I2', port=1)
            with MidiInstrument(id='P11-I2'):
                MidiChannel(14)
                MidiProgram(58)
                Volume(48.8189)
                Pan(0.0)
            MidiDevice(None, id='P11-I3', port=1)
            with MidiInstrument(id='P11-I3'):
                MidiChannel(15)
                MidiProgram(44)
                Volume(49.6063)
                Pan(0.0)
            MidiDevice(None, id='P11-I4', port=1)
            with MidiInstrument(id='P11-I4'):
                MidiChannel(16)
                MidiProgram(58)
                Volume(54.3307)
                Pan(0.0)
            MidiDevice(None, id='P11-I5', port=2)
            with MidiInstrument(id='P11-I5'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(59.0551)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P12'):
            PartName('Cembalo\nContinuo')
            PartAbbreviation('CEM')
            with ScoreInstrument(id='P12-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P12-I1', port=2)
            with MidiInstrument(id='P12-I1'):
                MidiChannel(2)
                MidiProgram(7)
                Volume(23.622)
                Pan(-90.0)
        with ScorePart(id='P13'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P13-I1'):
                InstrumentName('Organ')
            with ScoreInstrument(id='P13-I2'):
                InstrumentName('Organ')
            MidiDevice(None, id='P13-I1', port=2)
            with MidiInstrument(id='P13-I1'):
                MidiChannel(3)
                MidiProgram(75)
                Volume(29.9213)
                Pan(-27.0)
            MidiDevice(None, id='P13-I2', port=2)
            with MidiInstrument(id='P13-I2'):
                MidiChannel(4)
                MidiProgram(22)
                Volume(29.1339)
                Pan(-27.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P14'):
            PartName('Bassoon\nContinuo')
            PartAbbreviation('BSN\nB.C.')
            with ScoreInstrument(id='P14-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P14-I1', port=2)
            with MidiInstrument(id='P14-I1'):
                MidiChannel(5)
                MidiProgram(71)
                Volume(31.4961)
                Pan(0.0)
        with ScorePart(id='P15'):
            PartName('Bassono\nGrosso\nContinuo')
            PartAbbreviation('BSN\nB.C.')
            with ScoreInstrument(id='P15-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P15-I1', port=2)
            with MidiInstrument(id='P15-I1'):
                MidiChannel(6)
                MidiProgram(71)
                Volume(32.2835)
                Pan(26.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P16'):
            PartName('Violoncello\nContinuo')
            PartAbbreviation('VCO\nB.C.')
            with ScoreInstrument(id='P16-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P16-I1', port=2)
            with MidiInstrument(id='P16-I1'):
                MidiChannel(7)
                MidiProgram(43)
                Volume(30.7087)
                Pan(90.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P17'):
            PartName('Violoncelli\nContinuo')
            PartAbbreviation('VCI\nB.C.')
            with ScoreInstrument(id='P17-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P17-I1', port=2)
            with MidiInstrument(id='P17-I1'):
                MidiChannel(8)
                MidiProgram(43)
                Volume(32.2835)
                Pan(0.0)
        with ScorePart(id='P18'):
            PartName('Contrabassi\nContinuo')
            PartAbbreviation('CBI\nB.C.')
            with ScoreInstrument(id='P18-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P18-I1', port=2)
            with MidiInstrument(id='P18-I1'):
                MidiChannel(9)
                MidiProgram(44)
                Volume(32.2835)
                Pan(54.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=252.11):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(126.36)
                        RightMargin(0.0)
                    TopSystemDistance(303.85)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('54', default_x=-39.32, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=54.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.03)
                        RightMargin(-0.0)
                    SystemDistance(202.05)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.03)
                        RightMargin(0.0)
                    SystemDistance(202.05)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.03)
                        RightMargin(0.0)
                    SystemDistance(202.05)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=91.12, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.13, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.49, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.84, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.19, default_y=0.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.54, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.89, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.25, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.6, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.95, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=447.2, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.55, default_y=5.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.9, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=478.37):
            with Note(default_x=15.8, default_y=0.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.35, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.02, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.57, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.13, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.68, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.23, default_y=0.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.79, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.34, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.9, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.45, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.0, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=362.56, default_y=5.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=391.11, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.66, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.22, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.34, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.88, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.42, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.96, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.5, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.04, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.58, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.13, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.67, default_y=-35.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.21, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.75, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=322.29, default_y=0.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.83, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.37, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.91, default_y=-35.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-10.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.91, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.57, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.48, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.39, default_y=-30.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.3, default_y=-35.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.21, default_y=-40.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.12, default_y=-45.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.03, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.73, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.63, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.54, default_y=10.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=375.45, default_y=-5.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.36, default_y=-15.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.27, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.18, default_y=-40.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.03)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=62.51, default_y=-25.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.03)
                        RightMargin(0.0)
                    SystemDistance(1200.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=91.12, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.13, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.49, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.84, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.19, default_y=-105.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.54, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.89, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.25, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.6, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.95, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=447.2, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.55, default_y=-100.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.9, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=478.37):
            with Note(default_x=15.8, default_y=-105.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.35, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.02, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.57, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.13, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.68, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.23, default_y=-105.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.79, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.34, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.9, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.45, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.0, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=362.56, default_y=-100.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=391.11, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.66, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.22, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.34, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.88, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.42, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.96, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.5, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.04, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.58, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.13, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.67, default_y=-140.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.21, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.75, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=322.29, default_y=-105.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.83, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.37, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.91, default_y=-140.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-115.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.91, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.57, default_y=-125.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.48, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.39, default_y=-135.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.3, default_y=-140.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.21, default_y=-145.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.12, default_y=-150.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.03, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.73, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.63, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.54, default_y=-95.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=375.45, default_y=-110.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.36, default_y=-120.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.27, default_y=-130.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.18, default_y=-145.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.51, default_y=-165.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.13, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-230.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-240.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=362.56, default_y=-205.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=448.22, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=-210.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-225.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-235.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-245.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-220.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-215.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.51, default_y=-270.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=91.12, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.13, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.49, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.84, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.19, default_y=-315.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.54, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.89, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.25, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.6, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.95, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=447.2, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.55, default_y=-310.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.9, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=478.37):
            with Note(default_x=15.8, default_y=-315.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.35, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.02, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.57, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.13, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.68, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.23, default_y=-315.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.79, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.34, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.9, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.45, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.0, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=362.56, default_y=-310.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=391.11, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.66, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.22, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.34, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.88, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.42, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.96, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.5, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.04, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.58, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.13, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.67, default_y=-350.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.21, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.75, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=322.29, default_y=-315.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.83, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.37, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.91, default_y=-350.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-325.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.91, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.57, default_y=-335.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.48, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.39, default_y=-345.0, dynamics=101.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.3, default_y=-350.0, dynamics=101.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.21, default_y=-355.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.12, default_y=-360.0, dynamics=101.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.03, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.73, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.63, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.54, default_y=-305.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=375.45, default_y=-320.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.36, default_y=-330.0, dynamics=101.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.27, default_y=-340.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.18, default_y=-355.0, dynamics=101.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=62.51, default_y=-375.0, dynamics=101.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-455.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-450.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-460.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=-455.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=134.13, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-455.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-465.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-465.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=362.56, default_y=-440.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=448.22, default_y=-440.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-450.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=-450.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=220.13, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-455.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-455.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-440.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-440.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-440.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=-460.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-445.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-355.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=91.12, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.78, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.13, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.49, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.84, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.19, default_y=-495.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.54, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=299.89, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.25, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.6, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.95, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=447.2, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.55, default_y=-490.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.9, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=478.37):
            with Note(default_x=15.8, default_y=-495.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.35, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.02, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.57, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.13, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.68, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.23, default_y=-495.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.79, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=248.34, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.9, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.45, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.0, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=362.56, default_y=-490.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=391.11, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.66, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=448.22, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.34, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.88, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.42, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.96, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.5, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.04, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.58, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.13, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.67, default_y=-530.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.21, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.75, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=322.29, default_y=-495.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.83, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.37, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.91, default_y=-530.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-505.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.91, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.57, default_y=-515.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.48, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.39, default_y=-525.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.3, default_y=-530.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.21, default_y=-535.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.12, default_y=-540.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=255.03, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.73, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.63, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.54, default_y=-485.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=375.45, default_y=-500.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.36, default_y=-510.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.27, default_y=-520.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.18, default_y=-535.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(420.0)
            with Note(default_x=62.51, default_y=-450.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                Instruments(2)
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Evangelista', default_y=8.9, relative_x=0.32, relative_y=6.81, font_weight='bold', font_size='12')
            with Note(default_x=106.64, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.2, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=149.75, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=171.31, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=205.79, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=227.35, default_y=5.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=202.27):
            with Note(default_x=15.32, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='3', width=205.31):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
            with Note(default_x=95.93, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=118.91, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.9, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=164.88, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.55, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=181.09):
            with Note(default_x=12.94, default_y=-30.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.26, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.97, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.69, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.83, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.54, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.26, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=255.25):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=107.14, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=136.44, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.75, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=195.05, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=224.35, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=302.5):
            with Note(default_x=23.87, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.12, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.61, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.13, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.66, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=187.91, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.43, default_y=5.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.96, default_y=10.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=258.21, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.73, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=246.46):
            with Note(default_x=12.72, default_y=-30.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.27, default_y=-30.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=101.37, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=131.26, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.29, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=185.76, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=215.31, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=410.34, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='19', width=514.01):
            with Note(default_x=17.23, default_y=10.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.25, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.64, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.03, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.41, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.8, default_y=5.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.19, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=278.58, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=367.98, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=402.37, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=457.39, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-565.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='21', width=478.37):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='22', width=426.05):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='23', width=492.69):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=120.57, default_y=-515.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=162.8, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=189.19, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.05, default_y=-545.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=260.28, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=302.51, default_y=-530.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=354.0, default_y=-520.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='25', width=290.13):
            with Note(default_x=12.94, default_y=-520.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=49.2, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=179.74, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=216.01, default_y=-550.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=252.27, default_y=-545.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=529.55):
            with Note(default_x=12.36, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.2, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=104.03, default_y=-530.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.87, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.2, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.54, default_y=-515.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.88, default_y=-520.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=279.77, default_y=-525.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=300.61, default_y=-520.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.94, default_y=-525.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=354.78, default_y=-530.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=375.61, default_y=-525.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=408.95, default_y=-520.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=429.78, default_y=-525.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=450.62, default_y=-530.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=483.95, default_y=-525.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=504.79, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='27', width=732.29):
            with Note(default_x=16.2, default_y=-530.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.62, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=71.65, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=95.69, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.11, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=151.14, default_y=-545.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=180.01, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.43, default_y=-535.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=235.46, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=264.33, default_y=-545.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.75, default_y=-540.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=319.78, default_y=-550.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=349.68, default_y=-545.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
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
            with Note(default_x=376.78, default_y=-550.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.88, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=443.57, default_y=-550.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=470.67, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=500.57, default_y=-560.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=542.9, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
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
            with Note(default_x=570.0, default_y=-550.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=597.1, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=636.8, default_y=-560.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=663.9, default_y=-555.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=691.0, default_y=-565.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
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
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=70.75, default_y=-35.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.34, default_y=-40.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.92, default_y=-45.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.8, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=303.39, default_y=-30.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.98, default_y=-35.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
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
            with Note(default_x=428.85, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P7-I2')
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
            with Note(default_x=482.44, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=536.03, default_y=-25.0, dynamics=117.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=607.91, default_y=-5.0, dynamics=117.78):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=661.49, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=715.08, default_y=-15.0, dynamics=117.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P7-I2')
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
            with Note(default_x=786.96, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=905.17, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=967.3, default_y=5.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=1062.34, default_y=5.0, dynamics=117.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=1139.09, default_y=-10.0, dynamics=117.78):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P7-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(1)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(630.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-645.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=-620.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.13, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-645.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-640.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-650.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=362.56, default_y=-615.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=448.22, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=-620.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-635.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-645.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-655.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-630.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-625.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-565.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-740.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-735.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-745.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=-740.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.13, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-740.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-750.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-750.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=362.56, default_y=-725.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=448.22, default_y=-725.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-735.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=-735.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-740.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-740.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-725.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-725.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-725.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=-745.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-730.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
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
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-835.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=134.13, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=362.56, default_y=-870.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=448.22, default_y=-860.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-865.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-850.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-845.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-840.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-855.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P11'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                Instruments(5)
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Pilatus', default_y=7.47, relative_x=11.68, relative_y=13.3, font_weight='bold', font_size='12')
            with Note(default_x=69.91, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=92.89, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.87, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=138.86, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.84, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.51, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=205.31):
            with Note(default_x=18.36, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.34, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=181.09):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Jesus', default_y=2.35, relative_x=3.48, relative_y=5.54, font_weight='bold', font_size='12')
            with Note(default_x=45.07, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.2, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=124.99, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.66, default_y=-135.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.33, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=238.89):
            with Note(default_x=15.32, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.43, default_y=-145.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=93.66, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=119.78, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.1, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.42, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.74, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=185.06, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=211.17, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=292.97):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.03, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=74.92, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=104.63, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.19, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.76, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=171.47, default_y=-140.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=219.74, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.63, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.2, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=225.78):
            with Note(default_x=17.23, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.04, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.74, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.43, default_y=-90.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=133.7, default_y=-90.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.51, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=275.21):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.35, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.99, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.62, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=129.31, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.82, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=190.72, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=245.98, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=60.71, default_y=-90.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=95.0, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=129.29, default_y=-85.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.59, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.1, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.53, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=238.96, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.25, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I3')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=285.45):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Pilatus', default_y=5.23, relative_x=-4.7, relative_y=5.54, font_weight='bold', font_size='12')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=239.97, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.68, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=255.25):
            with Note(default_x=18.64, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.54, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=44.02, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.68, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.34, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.0, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.66, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.32, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=197.98, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=262.78):
            with Note(default_x=15.32, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=83.93, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=112.82, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.71, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.6, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.66, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=218.55, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.01, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Pilatus', relative_y=40.0)
            with Note(default_x=63.09, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.93, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.6, default_y=-125.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=270.44, default_y=-90.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=322.27, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=374.11, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=425.94, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=458.34, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=460.82):
            with Note(default_x=15.8, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.94, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=175.22, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.43, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=241.65, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=306.45, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=339.66, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=392.8, default_y=-120.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=426.01, default_y=-115.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=466.79):
            with Note(default_x=12.72, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.57, default_y=-130.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.41, default_y=-100.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.25, default_y=-105.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.53, default_y=-110.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=245.81, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=300.65, default_y=-95.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tutti', default_y=25.77, font_weight='bold', font_size='12')
            with Note(default_x=123.78, default_y=-930.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=182.49, default_y=-930.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=241.19, default_y=-965.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=-935.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=387.95, default_y=-925.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=417.85, default_y=-945.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=191.23, default_y=-965.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.34, default_y=-950.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-950.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=362.56, default_y=-940.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=419.66, default_y=-950.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-935.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=92.42, default_y=-935.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=117.96, default_y=-935.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=169.04, default_y=-970.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=220.13, default_y=-955.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-960.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-965.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-970.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-975.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=110.48, default_y=-975.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=139.39, default_y=-940.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=255.03, default_y=-945.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=346.54, default_y=-980.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.45, default_y=-980.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P11-I5')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P12'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
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
            with Note(default_x=84.73, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=84.73, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=84.73, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=170.94, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=170.94, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=170.94, default_y=-20.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=81.77, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=202.27):
            with Note(default_x=12.0, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-15.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='3', width=205.31):
            with Note(default_x=15.04, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.04, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.04, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
        with Measure(number='4', width=181.09):
            with Note(default_x=12.94, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-10.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.94, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='10', width=285.45):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=86.69, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.69, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=86.69, default_y=-20.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=160.9, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=160.9, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=86.69, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=160.9, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=255.25):
            with Note(default_x=15.32, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.32, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Note(default_x=15.32, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.32, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='12', width=302.5):
            with Note(default_x=23.51, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=23.51, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=23.51, default_y=-20.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=156.3, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=156.3, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=156.3, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=20.55, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
        with Measure(number='13', width=246.46):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=185.76, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=185.76, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=12.36, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=12.36, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=131.26, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=131.26, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=131.26, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=185.76, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=215.31, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=215.31, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=215.31, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=131.26, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=185.76, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=225.24):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=120.64, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.04, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=15.04, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.04, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
        with Measure(number='15', width=262.78):
            with Note(default_x=12.0, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=62.73, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=62.73, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=62.73, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=270.08, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=270.08, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=270.08, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=59.77, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='17', width=460.82):
            with Note(default_x=15.44, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.44, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.44, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=241.29, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=241.29, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=15.44, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=241.29, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=466.79):
            with Note(default_x=12.36, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=245.45, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=245.45, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=258.04, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=245.45, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=514.01):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=402.37, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=402.37, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=16.87, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=16.87, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=16.87, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=278.58, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=278.58, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=278.58, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=333.6, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=333.6, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=333.6, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=402.37, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=457.39, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=457.39, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=457.39, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=16.87, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=278.58, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=333.6, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=402.37, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-985.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=61.77, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=61.77, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=61.77, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=61.77, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='21', width=478.37):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='22', width=426.05):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='23', width=492.69):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=120.21, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=132.8, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=132.8, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=302.51, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=217.69, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('3')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=230.28, default_y=-60.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('3')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=120.57, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=217.69, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='25', width=290.13):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=85.46, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=85.46, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=85.46, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=143.12, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=143.12, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=143.12, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=85.46, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.12, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=529.55):
            with Note(default_x=12.0, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=216.54, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=300.61, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=216.18, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=216.18, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=216.54, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=333.94, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=375.61, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=429.78, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=450.62, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=504.79, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=732.29):
            with Note(default_x=16.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=95.69, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=95.69, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=107.55, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=180.01, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=180.01, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=180.01, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=264.33, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=264.33, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=264.33, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=349.68, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=349.68, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=349.68, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=443.57, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=443.57, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=443.57, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=542.9, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=542.9, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=542.9, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=636.8, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=636.8, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=636.8, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=16.2, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=71.65, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=95.69, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=151.14, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=180.01, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=235.46, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=264.33, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=319.78, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=349.68, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=419.54, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=443.57, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=516.24, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=542.9, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=612.77, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=636.8, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=706.66, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=70.75, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.75, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=428.85, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=428.85, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=428.85, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=786.96, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=786.96, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=786.96, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=905.17, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=905.17, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=905.17, default_y=-15.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=1062.34, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=1062.34, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=1062.34, default_y=-20.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=1139.09, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=1139.09, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=1139.09, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(48.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=70.75, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=202.28, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=249.8, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=381.33, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=428.85, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=560.39, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=607.91, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=739.44, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=786.96, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=857.64, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=905.17, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=1014.82, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=1062.34, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=1139.09, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='29', width=716.52):
            with Note(default_x=12.0, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P13'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(-2)
                with Time():
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
                with Transpose():
                    Diatonic(1)
                    Chromatic(2.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=181.09):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=45.07, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=45.07, default_y=-55.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.93, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=45.07, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=81.5, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=81.5, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(48.0)
            with Note(default_x=76.84, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Transpose():
                    Diatonic(1)
                    Chromatic(2.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Organo', default_y=11.89, relative_x=5.42, relative_y=6.55, font_weight='bold', font_size='12')
                Staff(2)
            with Note(default_x=45.07, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=76.84, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='5', width=238.89):
            with Note(default_x=19.62, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=19.62, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=185.06, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=185.06, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=185.06, default_y=-35.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(96.0)
            with Note(default_x=14.96, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(72.0)
                Tie(type='stop')
                Instrument(id='P13-I2')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='6', width=292.97):
            with Note(default_x=12.0, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(96.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-55.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(96.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(1)
            with Note(default_x=12.0, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Instrument(id='P13-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='7', width=225.78):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=187.32, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=187.32, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=17.23, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=17.23, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=77.74, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=77.74, default_y=-55.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=77.74, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=187.32, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Instrument(id='P13-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=224.18, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Instrument(id='P13-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.18, default_y=-55.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=224.18, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.23, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=77.74, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=187.32, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=275.21):
            with Note(default_x=12.36, default_y=-75.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-65.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=128.95, default_y=-75.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=128.95, default_y=-55.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=128.95, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.36, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=128.95, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=60.71, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.71, default_y=-50.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.71, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=129.29, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=129.29, default_y=-45.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=129.29, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=307.54, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=307.54, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=307.54, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=354.69, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=354.69, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=354.69, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=60.71, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=129.29, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=307.54, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=285.45):
            with Note(default_x=12.12, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.12, default_y=-40.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=12.12, default_y=-25.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(24.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=12.12, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=123.78, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.49, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=241.19, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=358.6, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=387.95, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=417.85, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=123.78, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=182.49, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=241.19, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=358.6, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=387.95, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=417.85, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=77.02, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=134.13, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=191.23, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=248.34, default_y=-25.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=305.45, default_y=-35.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=362.56, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=448.22, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=77.02, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=134.13, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=191.23, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=248.34, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=305.45, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=362.56, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=448.22, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=169.04, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=220.13, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=271.21, default_y=-20.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=322.29, default_y=-30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=373.37, default_y=-40.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=15.8, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=169.04, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=220.13, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=271.21, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=322.29, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=373.37, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=110.48, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=139.39, default_y=-15.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=255.03, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=346.54, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=375.45, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=20.0, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=110.48, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=139.39, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=255.03, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=346.54, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=375.45, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Instrument(id='P13-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P14'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.49, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=241.19, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=387.95, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=417.85, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.13, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=191.23, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.34, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=305.45, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note(default_x=362.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=448.22, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=271.21, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=322.29, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=373.37, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=110.48, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=139.39, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=346.54, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=375.45, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=62.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P15'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.49, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=241.19, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=387.95, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=417.85, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.13, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=191.23, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.34, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=305.45, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note(default_x=362.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=448.22, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=271.21, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=322.29, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=373.37, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=110.48, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=139.39, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=346.54, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=375.45, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=62.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P16'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=81.77, default_y=-255.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='2', width=202.27):
            with Note(default_x=12.0, default_y=-235.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='3', width=205.31):
            with Note(default_x=15.04, default_y=-255.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='4', width=181.09):
            with Note(default_x=12.94, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.07, default_y=-230.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.84, default_y=-250.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='5', width=238.89):
            with Note(default_x=12.0, default_y=-250.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='6', width=292.97):
            with Note(default_x=12.0, default_y=-250.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='7', width=225.78):
            with Note(default_x=17.23, default_y=-255.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=77.74, default_y=-250.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=187.32, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=275.21):
            with Note(default_x=12.36, default_y=-230.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=128.95, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=60.71, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.29, default_y=-215.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=307.54, default_y=-220.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='10', width=285.45):
            with Note(default_x=12.12, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=160.9, default_y=-235.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='11', width=255.25):
            with Note(default_x=15.32, default_y=-230.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=302.5):
            with Note(default_x=20.55, default_y=-230.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='13', width=246.46):
            with Note(default_x=12.36, default_y=-225.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=131.26, default_y=-235.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=185.76, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=225.24):
            with Note(default_x=15.04, default_y=-250.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='15', width=262.78):
            with Note(default_x=12.0, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=59.77, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='17', width=460.82):
            with Note(default_x=15.44, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=241.29, default_y=-225.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=466.79):
            with Note(default_x=12.36, default_y=-225.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=245.45, default_y=-225.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=514.01):
            with Note(default_x=16.87, default_y=-235.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=278.58, default_y=-230.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=333.6, default_y=-240.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=402.37, default_y=-245.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(1050.0)
            with Note(default_x=61.77, default_y=-1070.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=299.89, default_y=-1075.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=478.37):
            with Note(default_x=15.8, default_y=-1070.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.02, default_y=-1070.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=134.13, default_y=-1060.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-1070.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=248.34, default_y=-1055.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=305.45, default_y=-1090.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=362.56, default_y=-1080.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=419.66, default_y=-1090.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=-1075.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.88, default_y=-1075.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=117.96, default_y=-1065.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=169.04, default_y=-1075.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=220.13, default_y=-1060.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=271.21, default_y=-1095.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=322.29, default_y=-1080.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=373.37, default_y=-1095.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=-1080.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.57, default_y=-1085.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=139.39, default_y=-1080.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=254.67, default_y=-1085.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(630.0)
            with Note(default_x=62.51, default_y=-665.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.57, default_y=-675.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=217.69, default_y=-670.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='25', width=290.13):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=85.46, default_y=-665.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.12, default_y=-650.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='26', width=529.55):
            with Note(default_x=12.0, default_y=-665.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=216.54, default_y=-660.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=333.94, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=375.61, default_y=-650.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=429.78, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=450.62, default_y=-660.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=504.79, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='27', width=732.29):
            with Note(default_x=16.2, default_y=-655.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.65, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=95.69, default_y=-650.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.14, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=180.01, default_y=-645.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.46, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=264.33, default_y=-650.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.78, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=349.68, default_y=-655.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=419.54, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=443.57, default_y=-650.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=516.24, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=542.9, default_y=-645.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=612.77, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=636.8, default_y=-655.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=706.66, default_y=-635.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=70.75, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.28, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=249.8, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.33, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=428.85, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=560.39, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=607.91, default_y=-160.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=739.44, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=786.96, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=857.64, default_y=-120.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=905.17, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1014.82, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=1062.34, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=1139.09, default_y=-160.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='29', width=716.52):
            with Note(default_x=12.0, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P17'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-1090.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.49, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=241.19, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=387.95, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=417.85, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.13, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=191.23, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.34, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=305.45, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note(default_x=362.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=448.22, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=271.21, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=322.29, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=373.37, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=110.48, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=139.39, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=346.54, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=375.45, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-670.0)
            with Note(default_x=62.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P18'):
        with Measure(number='1', width=252.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='2', width=202.27):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='3', width=205.31):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='4', width=181.09):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='5', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='6', width=292.97):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='7', width=225.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='8', width=275.21):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='9', width=356.29):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='10', width=285.45):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='11', width=255.25):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='12', width=302.5):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='13', width=246.46):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='14', width=225.24):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='15', width=262.78):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='16', width=492.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='17', width=460.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='18', width=466.79):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='19', width=514.01):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='20', width=536.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.78, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=182.49, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=241.19, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=358.6, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=387.95, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=417.85, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=478.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.02, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=134.13, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=191.23, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=248.34, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=305.45, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note(default_x=362.56, default_y=-5.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=448.22, default_y=5.0, dynamics=106.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='22', width=426.05):
            with Note(default_x=15.8, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=169.04, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=220.13, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=271.21, default_y=0.0, dynamics=106.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=322.29, default_y=15.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=373.37, default_y=20.0, dynamics=106.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='23', width=492.69):
            with Note(default_x=20.0, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=110.48, default_y=25.0, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=139.39, default_y=30.0, dynamics=106.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=255.03, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=346.54, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=375.45, default_y=10.0, dynamics=106.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=381.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=62.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=290.13):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='26', width=529.55):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='27', width=732.29):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='28', width=1217.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='29', width=716.52):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')