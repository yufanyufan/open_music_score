with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 245')
        WorkTitle('Saint John Passion, 1724, 1725, 1732, 1749, 1750 and possibly others')
    MovementNumber('BWV 245 NBA #10')
    MovementTitle('Derselbige Jünger war dem Hohenpriester bekannt')
    with Identification():
        Creator('Edward J. Maurath', type='arranger')
        Creator('Johann Sebastian Bach (1685--1750)', type='composer')
        Creator('Saint John, Gospel of, Chap 18 & 19', type='lyricist')
        Creator('Baroque Passion Oratorio', type='poet')
        Creator('Martin Luther, 1521', type='translator')
        Rights('Sequenced by Edward J. Maurath')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(8.88)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2675.68)
            PageWidth(1891.89)
            with PageMargins(type='both'):
                LeftMargin(45.045)
                RightMargin(45.045)
                TopMargin(45.045)
                BottomMargin(90.0902)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Derselbige Jünger war dem Hohenpriester bekannt', default_x=945.945, default_y=2630.63, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Recitative for Evangelista, Servus, Ancilla, Petrus, Jesus, NBA #10 from BWV 245, Saint John Passion\n', default_x=945.945, default_y=2585.59, justify='center', valign='top', font_size='14')
        CreditWords('More MuseScore files at http://bach.ejmaurath.com\n')
        CreditWords('I reccommend AGAINST loading this into Musescore 3')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)', default_x=1846.84, default_y=2449.55, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Martin Luther, Gospel of John, Chap 18 & 19, Anno Domini 1521', default_x=45.045, default_y=2449.55, justify='left', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=945.945, default_y=90.0902, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Evangelista')
            PartAbbreviation('EVG')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Tenor')
            with ScoreInstrument(id='P1-I2'):
                InstrumentName('Recorder')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(86)
                Volume(0.0)
                Pan(0.0)
            MidiDevice(None, id='P1-I2', port=1)
            with MidiInstrument(id='P1-I2'):
                MidiChannel(2)
                MidiProgram(42)
                Volume(66.1417)
                Pan(19.0)
        with ScorePart(id='P2'):
            PartName('Servus')
            PartAbbreviation('SRV')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Tenor')
            with ScoreInstrument(id='P2-I2'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(3)
                MidiProgram(55)
                Volume(0.0)
                Pan(0.0)
            MidiDevice(None, id='P2-I2', port=1)
            with MidiInstrument(id='P2-I2'):
                MidiChannel(4)
                MidiProgram(69)
                Volume(60.6299)
                Pan(19.0)
        with ScorePart(id='P3'):
            PartName('Ancilla\nPetrus\nJesus')
            PartAbbreviation('ANC\nPTR\nJES')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Soprano')
            with ScoreInstrument(id='P3-I2'):
                InstrumentName('Flute')
            with ScoreInstrument(id='P3-I3'):
                InstrumentName('Bassoon')
            with ScoreInstrument(id='P3-I4'):
                InstrumentName('Trombone')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(5)
                MidiProgram(125)
                Volume(0.0)
                Pan(0.0)
            MidiDevice(None, id='P3-I2', port=1)
            with MidiInstrument(id='P3-I2'):
                MidiChannel(6)
                MidiProgram(74)
                Volume(70.0787)
                Pan(0.0)
            MidiDevice(None, id='P3-I3', port=1)
            with MidiInstrument(id='P3-I3'):
                MidiChannel(7)
                MidiProgram(72)
                Volume(59.8425)
                Pan(-14.0)
            MidiDevice(None, id='P3-I4', port=1)
            with MidiInstrument(id='P3-I4'):
                MidiChannel(8)
                MidiProgram(71)
                Volume(70.0787)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Cembalo\nContinuo')
            PartAbbreviation('CEM\nB.C.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(9)
                MidiProgram(7)
                Volume(43.3071)
                Pan(-90.0)
        with ScorePart(id='P5'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG\nB.C.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Organ')
            with ScoreInstrument(id='P5-I2'):
                InstrumentName('Hand Bells')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(11)
                MidiProgram(20)
                Volume(0.0)
                Pan(0.0)
            MidiDevice(None, id='P5-I2', port=1)
            with MidiInstrument(id='P5-I2'):
                MidiChannel(12)
                MidiProgram(33)
                Volume(100.0)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Violoncello\nContinuo')
            PartAbbreviation('VCO\nB.C.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(13)
                MidiProgram(43)
                Volume(49.6063)
                Pan(90.0)
    with Part(id='P1'):
        with Measure(number='1', width=303.87):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(120.92)
                        RightMargin(0.0)
                    TopSystemDistance(251.08)
            with Attributes():
                Divisions(8.0)
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('52', default_x=-50.53, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=52.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Evangelista', default_y=11.66, relative_x=-1.01, relative_y=10.93, font_weight='bold', font_size='12')
            with Note(default_x=118.89, default_y=-45.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=144.17, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.77, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=195.63, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=211.3, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=233.9, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=256.5, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=279.1, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=193.59):
            with Note(default_x=16.2, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.31, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.42, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.53, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.2, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.06, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=168.82, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='3', width=177.61):
            with Note(default_x=16.2, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=35.79, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=55.39, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.98, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.64, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.31, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=133.25, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.84, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=174.53):
            with Note(default_x=12.0, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.33, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.66, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.99, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.65, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.32, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=124.65, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=231.77):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=36.86, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.52, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=68.19, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=92.68, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.35, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.81, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.31, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=181.18, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=205.67, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=177.75):
            with Note(default_x=16.2, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=61.32, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=80.32, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.32, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=118.32, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.32, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.98, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=238.92):
            with Note(default_x=22.84, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.73, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=91.49, default_y=-40.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.16, default_y=-40.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.83, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=145.71, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=175.61, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=198.49, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=214.16, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=182.84):
            with Note(default_x=12.72, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.81, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=69.98, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=108.45, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.08, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.22)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note(default_x=60.71, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.17, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.08, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.0, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.46, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=168.92, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=194.38, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.29, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=226.21, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=257.25, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='10', width=223.08):
            with Note(default_x=12.0, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.12, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=54.45, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=70.77, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=100.67, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.99, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.32, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=159.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=206.89):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=67.99, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=107.5, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.68, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.86, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=182.13, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='12', width=211.23):
            with Note(default_x=17.23, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.21, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.88, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=71.55, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.53, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=117.51, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=140.5, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='13', width=226.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='14', width=197.08):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=80.82, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=106.1, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='15', width=150.54):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=125.77, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='16', width=244.07):
            with Note(default_x=15.32, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.36, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=65.41, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=90.45, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.11, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.01, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.05, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.72, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.39, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=217.43, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(59.9)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=99.26, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=138.76, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.85, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.77, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.67, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=239.75, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=256.68, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.61, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=174.94):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=37.99, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.02, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.05, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=98.09, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.17, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='19', width=312.5):
            with Note(default_x=12.0, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.36, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=62.03, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=77.69, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Fermata(None, type='upright', default_y=14.05, relative_y=10.0)
                    with Articulations():
                        Staccato()
            with Note(default_x=99.24, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.8, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Fermata(None, type='upright', default_y=2.24, relative_y=10.0)
            with Note(default_x=150.69, default_y=-35.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=172.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=247.1):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=42.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.06, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.97, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=149.87, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=173.78, default_y=-40.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=197.69, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=221.59, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=204.59):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=35.9, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=59.44, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.98, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.65, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.31, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=226.98):
            with Note(default_x=15.32, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.13, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.79, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=71.46, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=96.26, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=126.16, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.97, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.77, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=200.58, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='23', width=263.34):
            with Note(default_x=15.32, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.39, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=60.94, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=78.48, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=106.55, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.42, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.96, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.51, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.05, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=205.6, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=233.67, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(59.9)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Note(default_x=63.09, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.45, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=141.93, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.29, default_y=10.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.96, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.62, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=219.98, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.65, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=143.62):
            with Note(default_x=12.94, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=186.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='27', width=203.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='28', width=224.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='29', width=266.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='30', width=272.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='31', width=183.6):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(59.9)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='33', width=389.25):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='34', width=334.54):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='35', width=372.36):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='36', width=320.03):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(59.9)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=106.06, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=135.0, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=163.93, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=192.86, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=221.79, default_y=5.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=251.69, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='38', width=315.02):
            with Note(default_x=17.23, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.49, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=57.75, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.59, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.85, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=172.74, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.16, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=237.58, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=269.99, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=290.26, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=277.42):
            with Note(default_x=17.23, default_y=-35.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.11, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=78.98, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=109.86, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=140.73, default_y=0.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=171.61, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=233.36, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=252.66, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=281.09):
            with Note(default_x=12.0, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.99, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.97, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.19, default_y=-25.0, dynamics=103.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=148.09, default_y=-35.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='41', width=277.28):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='42', width=308.86):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.67, default_y=-5.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.66, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.56, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=198.13, default_y=-30.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.12, default_y=-20.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=240.11, default_y=-10.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.68, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(59.9)
                        RightMargin(0.0)
                    SystemDistance(95.74)
            with Note(default_x=70.75, default_y=-15.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Instrument(id='P1-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='44', width=478.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='45', width=473.73):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='46', width=322.1):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=303.87):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
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
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=193.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=177.61):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='4', width=174.53):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='5', width=231.77):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='6', width=177.75):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='7', width=238.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='8', width=182.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='10', width=223.08):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='11', width=206.89):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='12', width=211.23):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='13', width=226.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='14', width=197.08):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='15', width=150.54):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='16', width=244.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='18', width=174.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='19', width=312.5):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='20', width=247.1):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='21', width=204.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='22', width=226.98):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='23', width=263.34):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='25', width=143.62):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='26', width=186.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='27', width=203.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='28', width=224.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='29', width=266.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='30', width=272.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='31', width=183.6):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='33', width=389.25):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='34', width=334.54):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='35', width=372.36):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='36', width=320.03):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='38', width=315.02):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='39', width=277.42):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='40', width=281.09):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Servus', relative_x=1.65, font_weight='bold', font_size='12')
            with Note(default_x=226.43, default_y=-125.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=256.33, default_y=-120.0, dynamics=103.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=277.28):
            with Note(default_x=17.23, default_y=-115.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.56, default_y=-115.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=79.89, default_y=-115.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=111.21, default_y=-110.0, dynamics=103.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.54, default_y=-105.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=173.87, default_y=-105.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.45, default_y=-105.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.03, default_y=-115.0, dynamics=103.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=244.35, default_y=-125.0, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=308.86):
            with Note(default_x=12.94, default_y=-100.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.52, default_y=-100.0, dynamics=103.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P2-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='44', width=478.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='45', width=473.73):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='46', width=322.1):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=303.87):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                Instruments(4)
                with Clef():
                    Sign('C')
                    Line(1)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=193.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=177.61):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='4', width=174.53):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='5', width=231.77):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='6', width=177.75):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='7', width=238.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='8', width=182.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='10', width=223.08):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='11', width=206.89):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='12', width=211.23):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Ancilla', default_y=10.62, relative_x=0.54, relative_y=0.44, font_weight='bold', font_size='12')
            with Note(default_x=186.46, default_y=-120.0, dynamics=104.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='13', width=226.67):
            with Note(default_x=12.72, default_y=-105.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.24, default_y=-105.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=63.77, default_y=-105.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=89.29, default_y=-100.0, dynamics=104.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.99, default_y=-95.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=148.51, default_y=-95.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=174.03, default_y=-85.0, dynamics=104.44):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=199.55, default_y=-105.0, dynamics=104.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=197.08):
            with Note(default_x=15.8, default_y=-90.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=-90.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Instrument(id='P3-I2')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Petrus', default_y=32.0, relative_x=-1.29, relative_y=4.76, font_weight='bold', font_size='12')
            with Note(default_x=146.86, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Instrument(id='P3-I3')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.31, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I3')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='15', width=150.54):
            with Note(default_x=12.94, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.14, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I3')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='16', width=244.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='18', width=174.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='19', width=312.5):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='20', width=247.1):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='21', width=204.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='22', width=226.98):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='23', width=263.34):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='25', width=143.62):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Jesus', default_y=7.52, relative_x=-4.24, relative_y=0.44, font_weight='bold', font_size='12')
            with Note(default_x=59.55, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=77.48, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=95.41, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=113.33, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=186.92):
            with Note(default_x=18.64, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.14, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=59.64, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=80.15, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=100.65, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.15, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=141.65, default_y=-135.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=162.15, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=203.67):
            with Note(default_x=15.32, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=62.7, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.37, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.03, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.7, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.77, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.83, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=178.9, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=224.07):
            with Note(default_x=12.36, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.05, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=57.74, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=80.43, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=103.12, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.81, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.17, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.83, default_y=-90.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.3, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=266.67):
            with Note(default_x=15.8, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.8, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=86.68, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.55, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.45, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.32, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=177.32, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.2, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=211.07, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=238.07, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=272.94):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Jesus', relative_x=2.35, relative_y=25.89)
            with Note(default_x=12.36, default_y=-140.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=39.06, default_y=-140.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=82.46, default_y=-140.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.15, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.84, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.53, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=159.23, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.92, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.78, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=231.49, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.18, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=183.6):
            with Note(default_x=15.32, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.95, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=83.0, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=103.06, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.11, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.17, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=158.83, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=63.09, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=179.11, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=215.36, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=251.61, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=287.87, default_y=-20.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=389.25):
            with Note(default_x=17.23, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=60.81, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.05, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.28, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.86, default_y=-15.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=202.44, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=246.02, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.26, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=300.49, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=344.07, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=334.54):
            with Note(default_x=17.23, default_y=-20.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.06, default_y=-20.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.96, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.48, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=154.31, default_y=-10.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=195.14, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.97, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=372.36):
            with Note(default_x=12.72, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.84, default_y=-15.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=139.09, default_y=-15.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=181.21, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.34, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.66, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=275.99, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=318.11, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=344.44, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=320.03):
            with Note(default_x=15.8, default_y=20.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.62, default_y=15.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=95.44, default_y=10.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=135.26, default_y=5.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=175.08, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=214.9, default_y=-5.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='38', width=315.02):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='39', width=277.42):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='40', width=281.09):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='41', width=277.28):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='42', width=308.86):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Words('Jesus', default_y=-58.59, relative_x=-1.18, relative_y=-1.14)
            with Note(default_x=148.32, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=204.73, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=261.14, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=317.55, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.81, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=388.07, default_y=-90.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='44', width=478.84):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=69.66, default_y=-90.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.63, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.59, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.93, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=225.9, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=259.86, default_y=-120.0, dynamics=97.78):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=314.21, default_y=-130.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=368.55, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=422.89, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=473.73):
            with Note(default_x=18.36, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=162.05, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.87, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=237.68, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.5, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.31, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.12, default_y=-95.0, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=388.94, default_y=-125.0, dynamics=97.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='46', width=322.1):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=65.72, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=119.08, default_y=-105.0, dynamics=97.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.44, default_y=-110.0, dynamics=97.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=205.79, default_y=-115.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=239.13, default_y=-100.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P3-I4')
                Voice('1')
                Type('quarter')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=303.87):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
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
            with Note(default_x=95.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=210.94, default_y=-80.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=210.94, default_y=-65.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=223.53, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=210.94, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=223.53, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=92.97, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
            with Note(default_x=92.97, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=74.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
            with Note(default_x=92.97, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=193.59):
            with Note(default_x=16.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=56.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=68.29, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.42, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=68.29, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=120.7, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=120.7, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=120.7, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.2, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=4.33, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=16.2, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.42, default_y=-40.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=120.7, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=177.61):
            with Note(default_x=16.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=16.2, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=67.25, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.39, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=105.95, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=105.95, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=118.54, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=105.95, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.84, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=105.95, default_y=-15.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=174.53):
            with Note(default_x=12.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=52.66, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=52.66, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=144.98, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=144.98, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=144.98, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=172.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=172.93, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=184.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=172.93, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-10.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.66, default_y=-30.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=144.98, default_y=-25.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=231.77):
            with Note(default_x=12.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=127.45, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=140.04, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=127.45, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=140.04, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=127.45, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='6', width=177.75):
            with Note(default_x=15.84, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.88, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='7', width=238.92):
            with Note(default_x=19.52, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=19.52, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Note(default_x=38.03, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Note(default_x=19.52, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.52, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
        with Measure(number='8', width=182.84):
            with Note(default_x=12.36, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=108.09, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=108.09, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=120.68, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=108.09, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=108.09, default_y=-25.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note(default_x=60.35, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=60.35, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=60.35, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=60.35, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=168.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=181.15, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=168.56, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=168.56, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=60.35, default_y=-30.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=168.56, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='10', width=223.08):
            with Note(default_x=12.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.77, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=82.64, default_y=-65.0):
                Chord()
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
            with Note(default_x=70.77, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.77, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.77, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=185.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=185.56, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=185.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=221.48, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=221.48, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=221.48, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=233.34, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=221.48, default_y=-30.0):
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
            with Note(default_x=12.0, default_y=-25.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=70.77, default_y=-45.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=185.56, default_y=-50.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=206.89):
            with Note(default_x=12.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=44.81, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.68, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=44.81, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=44.81, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=44.81, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.14, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=119.73, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.14, default_y=-50.0):
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
            with Note(default_x=107.14, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.14, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=44.45, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='12', width=211.23):
            with Note(default_x=16.87, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=29.46, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=117.15, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=117.15, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=117.15, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.87, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=117.15, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=226.67):
            with Note(default_x=12.36, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=122.62, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=122.62, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=122.62, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.21, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=122.62, default_y=-25.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=197.08):
            with Note(default_x=15.44, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.44, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=146.86, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=146.86, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.86, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=158.72, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.44, default_y=-30.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=146.86, default_y=-25.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=150.54):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=49.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=49.34, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=49.34, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.46, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.46, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.32, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.46, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=78.09, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=78.09, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=78.09, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=78.09, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=49.34, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=78.09, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=244.07):
            with Note(default_x=14.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.65, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=148.24, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.65, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=135.65, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.65, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=71.81, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=84.4, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=71.81, default_y=-45.0):
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
            with Note(default_x=71.81, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=212.31, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=224.9, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=212.31, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=212.31, default_y=-35.0):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=71.81, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=212.31, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=174.94):
            with Note(default_x=17.59, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.59, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=17.59, default_y=-45.0):
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
            with Note(default_x=17.59, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=97.73, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=110.31, default_y=-60.0):
                Chord()
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
            with Note(default_x=97.73, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=97.73, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=97.73, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.59, default_y=-20.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=97.73, default_y=-35.0):
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
        with Measure(number='19', width=312.5):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
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
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=218.85, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=218.85, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=218.85, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=248.49, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=248.49, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=260.35, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=248.49, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=278.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=278.12, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=278.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=218.85, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=278.12, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=247.1):
            with Note(default_x=18.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=18.0, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=197.69, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=197.69, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=197.69, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=18.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=197.69, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='21', width=204.59):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
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
            with Note(default_x=114.31, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.31, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=170.22, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=182.09, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.22, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.22, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=114.31, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=170.22, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=226.98):
            with Note(default_x=12.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=30.51, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='23', width=263.34):
            with Note(default_x=14.96, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=27.55, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=147.65, default_y=-60.0):
                Chord()
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
            with Note(default_x=135.06, default_y=-50.0):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=62.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=141.93, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.93, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.93, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.62, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.62, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.62, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=59.77, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='25', width=143.62):
            with Note(default_x=12.94, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
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
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='26', width=186.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='27', width=203.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='28', width=224.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='29', width=266.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='30', width=272.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='31', width=183.6):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=389.25):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='34', width=334.54):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='35', width=372.36):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='36', width=320.03):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=106.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.06, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.06, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.7, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='38', width=315.02):
            with Note(default_x=16.87, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=29.46, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-45.0):
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
            with Note(default_x=172.38, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=172.38, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=184.97, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=172.38, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=172.38, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='39', width=277.42):
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=78.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=78.98, default_y=-45.0):
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
            with Note(default_x=78.98, default_y=-30.0):
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
            with Note(default_x=140.73, default_y=-65.0):
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
            with Note(default_x=140.73, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=140.73, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=140.73, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=202.48, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.48, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.48, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.48, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.48, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=233.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=252.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=78.98, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=140.37, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='40', width=281.09):
            with Note(default_x=12.0, default_y=-65.0):
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
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
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
            with Note(default_x=77.97, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=77.97, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=148.09, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=159.95, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=148.09, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=148.09, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=193.44, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=193.44, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=205.31, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=193.44, default_y=-45.0):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=77.97, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=147.73, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='41', width=277.28):
            with Note(default_x=16.87, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=29.46, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-45.0):
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
            with Note(default_x=142.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=154.77, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=142.18, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=142.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=13.91, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='42', width=308.86):
            with Note(default_x=12.94, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.09, default_y=-65.0):
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
            with Note(default_x=80.09, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.09, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=91.96, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.73, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=70.75, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.75, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.75, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=70.75, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='44', width=478.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='45', width=473.73):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='46', width=322.1):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=303.87):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
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
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=193.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='3', width=177.61):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='4', width=174.53):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='5', width=231.77):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='6', width=177.75):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='7', width=238.92):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=182.84):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='10', width=223.08):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='11', width=206.89):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='12', width=211.23):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='13', width=226.67):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='14', width=197.08):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='15', width=150.54):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='16', width=244.07):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='18', width=174.94):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='19', width=312.5):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='20', width=247.1):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='21', width=204.59):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='22', width=226.98):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='23', width=263.34):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Organo', relative_x=101.39, relative_y=18.27, font_weight='bold', font_size='12')
                Staff(2)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='25', width=143.62):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=41.26, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=41.26, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=41.26, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=113.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.33, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=41.26, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=113.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=186.92):
            with Note(default_x=18.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.28, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=18.28, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=141.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.65, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=141.65, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=153.52, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.32, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='27', width=203.67):
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=224.07):
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=103.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.12, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=148.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=148.5, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=148.5, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.76, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='29', width=266.67):
            with Note(default_x=12.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=12.48, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=12.48, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=12.48, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=272.94):
            with Note(default_x=12.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=132.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=132.16, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=132.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=132.16, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=132.16, default_y=-50.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='31', width=183.6):
            with Note(default_x=14.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=82.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=82.64, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=82.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(32.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=62.73, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=62.73, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=62.73, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=178.74, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=178.74, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=178.74, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=178.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=59.77, default_y=-30.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='33', width=389.25):
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=29.1, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=115.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=115.28, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=127.15, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=115.28, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=202.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=202.44, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=202.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=300.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=300.49, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=300.49, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-30.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.28, default_y=-40.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=202.08, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=334.54):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.48, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.48, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=194.78, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=194.78, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=194.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=16.87, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=194.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='35', width=372.36):
            with Note(default_x=12.36, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=275.99, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=287.85, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=275.99, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.99, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=320.03):
            with Note(default_x=15.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.44, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.44, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=175.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=254.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=254.72, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=254.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=318.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=318.43, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=330.29, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=318.43, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=95.44, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
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
            with Note(default_x=254.72, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=59.77, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.77, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.77, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=59.77, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=59.77, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='38', width=315.02):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='39', width=277.42):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='40', width=281.09):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='41', width=277.28):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='42', width=308.86):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('5')
                Staff(2)
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=148.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=148.32, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=148.32, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=261.14, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=273.01, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=261.14, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=273.01, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=388.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=388.07, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=388.07, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=399.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=148.32, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=260.78, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='44', width=478.84):
            with Note(default_x=14.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=27.55, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=14.96, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=259.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=272.09, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=259.5, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=259.5, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(32.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='45', width=473.73):
            with Note(default_x=18.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=18.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=18.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=388.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.94, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.94, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=388.94, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(32.0)
            with Note(default_x=15.04, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Instrument(id='P5-I2')
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='46', width=322.1):
            with Note(default_x=12.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=239.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.13, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.13, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Instrument(id='P5-I2')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=239.13, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Instrument(id='P5-I2')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=303.87):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(315.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=92.97, default_y=-355.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=193.59):
            with Note(default_x=15.84, default_y=-355.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.7, default_y=-355.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=177.61):
            with Note(default_x=15.84, default_y=-355.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=105.95, default_y=-330.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='4', width=174.53):
            with Note(default_x=12.0, default_y=-325.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.66, default_y=-345.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=144.98, default_y=-340.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=231.77):
            with Note(default_x=12.0, default_y=-360.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=127.45, default_y=-355.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
        with Measure(number='6', width=177.75):
            with Note(default_x=12.88, default_y=-355.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=238.92):
            with Note(default_x=19.52, default_y=-335.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=182.84):
            with Note(default_x=12.36, default_y=-335.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=108.09, default_y=-340.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='9', width=282.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note(default_x=60.35, default_y=-240.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=168.56, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='10', width=223.08):
            with Note(default_x=12.0, default_y=-235.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.77, default_y=-255.0, dynamics=113.33):
                with Pitch():
                    Step('F')
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
            with Note(default_x=185.56, default_y=-260.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=206.89):
            with Note(default_x=12.94, default_y=-245.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.45, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=211.23):
            with Note(default_x=16.87, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=117.15, default_y=-230.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=226.67):
            with Note(default_x=12.36, default_y=-230.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=122.62, default_y=-235.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='14', width=197.08):
            with Note(default_x=15.44, default_y=-240.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=146.86, default_y=-235.0, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=150.54):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.34, default_y=-230.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.09, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=244.07):
            with Note(default_x=12.0, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='17', width=312.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=71.81, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=212.31, default_y=-125.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
        with Measure(number='18', width=174.94):
            with Note(default_x=17.59, default_y=-125.0, dynamics=113.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=97.73, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='19', width=312.5):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.85, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=278.12, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='20', width=247.1):
            with Note(default_x=15.04, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=204.59):
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=114.31, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=170.22, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=226.98):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='23', width=263.34):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='24', width=260.42):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=59.77, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='25', width=143.62):
            with Note(default_x=12.58, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=113.33, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=186.92):
            with Note(default_x=15.32, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='27', width=203.67):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=224.07):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.76, default_y=-250.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='29', width=266.67):
            with Note(default_x=12.48, default_y=-245.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=272.94):
            with Note(default_x=12.0, default_y=-245.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=132.16, default_y=-260.0, dynamics=113.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='31', width=183.6):
            with Note(default_x=12.0, default_y=-255.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='32', width=325.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.0)
            with Note(default_x=59.77, default_y=-135.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='33', width=389.25):
            with Note(default_x=17.23, default_y=-135.0, dynamics=113.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.28, default_y=-145.0, dynamics=113.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=202.08, default_y=-140.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=334.54):
            with Note(default_x=16.87, default_y=-140.0, dynamics=113.33):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=194.78, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='35', width=372.36):
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.99, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='36', width=320.03):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.44, default_y=-120.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=254.72, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='37', width=282.22):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=56.45, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='38', width=315.02):
            with Note(default_x=16.87, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=172.38, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='39', width=277.42):
            with Note(default_x=17.23, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=78.98, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=140.37, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='40', width=281.09):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.97, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.73, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='41', width=277.28):
            with Note(default_x=13.91, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(32.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='42', width=308.86):
            with Note(default_x=12.94, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.73, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='43', width=467.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=70.39, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=260.78, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='44', width=478.84):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
        with Measure(number='45', width=473.73):
            with Note(default_x=15.04, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Notations():
                    Tied(type='start')
        with Measure(number='46', width=322.1):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=239.13, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')